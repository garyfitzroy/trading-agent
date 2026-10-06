from __future__ import annotations

import math

import numpy as np
import pandas as pd


class MarketDataError(RuntimeError):
    pass


class MarketFeed:
    def __init__(self, source: str = "yfinance") -> None:
        self.source = (source or "yfinance").lower()

    def _synthetic_frame(self, symbol: str, days: int = 180, interval: str = "1h") -> pd.DataFrame:
        hours = max(24, int(days * 24))
        index = pd.date_range(end=pd.Timestamp.utcnow(), periods=hours, freq=interval)
        series = pd.Series(range(hours), index=index, dtype=float)
        base = 100.0
        price = base + (series * 0.35)
        data = pd.DataFrame(
            {
                "open": price,
                "high": price * 1.01,
                "low": price * 0.99,
                "close": price * 1.002,
                "volume": 1000 + (series * 4),
            },
            index=index,
        )
        data.index.name = "timestamp"
        return data

    def _normalize_frame(self, frame: pd.DataFrame) -> pd.DataFrame:
        columns = {col.lower(): col for col in frame.columns}
        needed = {"open": "open", "high": "high", "low": "low", "close": "close", "volume": "volume"}
        result = pd.DataFrame(index=frame.index)
        for key, target in needed.items():
            if key in columns:
                result[target] = pd.to_numeric(frame[columns[key]], errors="coerce")
            elif key == "volume" and "vol" in columns:
                result[target] = pd.to_numeric(frame[columns["vol"]], errors="coerce")
            else:
                raise ValueError(f"Missing required OHLCV column: {key}")
        result = result.dropna()
        result.index.name = "timestamp"
        return result

    def _fetch_yfinance(self, symbol: str, period: str, interval: str) -> pd.DataFrame:
        import yfinance as yf

        lookup = symbol.replace("/", "-") if "/" in symbol else symbol
        data = yf.download(
            tickers=lookup,
            period=period,
            interval=interval,
            auto_adjust=False,
            progress=False,
            threads=False,
            group_by="ticker",
        )
        if data.empty:
            raise ValueError(f"No finance data returned for {symbol}")
        return self._normalize_frame(data)

    def _fetch_ccxt(self, symbol: str, timeframe: str, limit: int = 100) -> pd.DataFrame:
        import ccxt

        exchange = ccxt.binance({"enableRateLimit": True})
        market = symbol.replace("/", "")
        candles = exchange.fetch_ohlcv(market, timeframe=timeframe, limit=limit)
        if not candles:
            raise ValueError(f"No candle data returned for {symbol}")

        data = pd.DataFrame(candles, columns=["timestamp", "open", "high", "low", "close", "volume"])
        data["timestamp"] = pd.to_datetime(data["timestamp"], unit="ms")
        data = data.set_index("timestamp")
        return self._normalize_frame(data)

    def load(self, symbol: str, days: int = 180, interval: str = "1h", period: str | None = None, allow_fallback: bool = True) -> pd.DataFrame:
        if period is None:
            period = "1y" if days >= 365 else "60d"

        if self.source == "synthetic":
            return self._synthetic_frame(symbol=symbol, days=days, interval=interval)

        try:
            if self.source in {"yfinance", "yf"}:
                return self._fetch_yfinance(symbol=symbol, period=period, interval=interval)
            if self.source in {"ccxt", "crypto"}:
                return self._fetch_ccxt(symbol=symbol, timeframe=interval, limit=max(50, min(days, 500)))
            raise MarketDataError(f"Unsupported market data source: {self.source}")
        except Exception as exc:
            if not allow_fallback:
                raise MarketDataError(f"Failed to fetch market data for {symbol}: {exc}") from exc
            return self._synthetic_frame(symbol=symbol, days=days, interval=interval)


def create_market_feed(source: str = "yfinance") -> MarketFeed:
    return MarketFeed(source=source)

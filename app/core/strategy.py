from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class Bar:
    timestamp: str
    open: float
    high: float
    low: float
    close: float
    volume: float


class BaseStrategy:
    def __init__(self, symbol: str, timeframe: str = "1h") -> None:
        self.symbol = symbol
        self.timeframe = timeframe
        self.position = 0
        self.entry_price: float | None = None
        self.bars: list[Bar] = []

    def on_bar(self, bar: Bar) -> None:
        raise NotImplementedError

    def buy(self) -> None:
        self.position = 1

    def sell(self) -> None:
        self.position = -1

    def flat(self) -> None:
        self.position = 0

    def close_prices(self) -> pd.Series:
        return pd.Series([bar.close for bar in self.bars], dtype=float)

    def rsi(self, period: int = 14) -> float:
        closes = self.close_prices()
        if len(closes) < period + 1:
            return 50.0

        delta = closes.diff()
        gains = delta.clip(lower=0)
        losses = (-delta).clip(lower=0)

        avg_gain = gains.rolling(window=period, min_periods=period).mean().iloc[-1]
        avg_loss = losses.rolling(window=period, min_periods=period).mean().iloc[-1]

        if avg_loss == 0:
            return 100.0

        rs = avg_gain / avg_loss
        return 100.0 - (100.0 / (1.0 + rs))

    def macd(self, fast: int = 12, slow: int = 26, signal: int = 9) -> tuple[float, float, float]:
        closes = self.close_prices()
        if len(closes) < slow:
            return 0.0, 0.0, 0.0

        ema_fast = closes.ewm(span=fast, adjust=False).mean()
        ema_slow = closes.ewm(span=slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        hist = macd_line - signal_line
        return float(macd_line.iloc[-1]), float(signal_line.iloc[-1]), float(hist.iloc[-1])

from __future__ import annotations

from app.core.backtest import BacktestEngine
from app.core.strategy import BaseStrategy
from app.data.feed import MarketFeed
from app.strategies.rsi import RSI


def run_backtest(symbol: str = "BTC/USD", strategy: type[BaseStrategy] = RSI, days: int = 180) -> dict[str, object]:
    feed = MarketFeed(source="synthetic")
    data = feed.load(symbol=symbol, days=days)
    engine = BacktestEngine(strategy, data)
    return engine.run()

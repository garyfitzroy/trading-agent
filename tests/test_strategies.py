from __future__ import annotations

from app.core.strategy import Bar
from app.strategies.macd import MACD
from app.strategies.rsi import RSI


def _build_price_series(start: float, drift: float, count: int):
    prices: list[float] = []
    current = start
    for idx in range(count):
        prices.append(current)
        current += drift
    return prices


def test_rsi_strategy_uses_oversold_signal() -> None:
    strategy = RSI("BTC/USD")
    price = 100.0
    for idx in range(60):
        price -= 0.5
        strategy.on_bar(
            Bar(
                timestamp=str(idx),
                open=price,
                high=price * 1.01,
                low=price * 0.99,
                close=price,
                volume=10_000,
            )
        )

    assert strategy.position == 1


def test_macd_strategy_uses_uptrend_signal() -> None:
    strategy = MACD("BTC/USD")
    price = 100.0
    for idx in range(80):
        price += 0.6
        strategy.on_bar(
            Bar(
                timestamp=str(idx),
                open=price,
                high=price * 1.01,
                low=price * 0.99,
                close=price,
                volume=10_000,
            )
        )

    assert strategy.position == 1

from __future__ import annotations

from dataclasses import dataclass


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

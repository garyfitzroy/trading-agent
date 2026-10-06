from __future__ import annotations

from app.core.strategy import BaseStrategy


class SMACrossover(BaseStrategy):
    def __init__(self, symbol: str, timeframe: str = "1h") -> None:
        super().__init__(symbol, timeframe)
        self.short_window = 10
        self.long_window = 30

    def on_bar(self, bar) -> None:
        if len(self.bars) < self.long_window:
            self.bars.append(bar)
            return
        self.bars.append(bar)
        del self.bars[0]
        closes = [entry.close for entry in self.bars]
        short_ma = sum(closes[-self.short_window:]) / self.short_window
        long_ma = sum(closes[-self.long_window:]) / self.long_window
        if short_ma > long_ma:
            self.buy()
        elif short_ma < long_ma:
            self.sell()
        else:
            self.flat()

from __future__ import annotations

from app.core.strategy import BaseStrategy


class MACD(BaseStrategy):
    def __init__(self, symbol: str, timeframe: str = "1h", fast: int = 12, slow: int = 26, signal: int = 9) -> None:
        super().__init__(symbol, timeframe)
        self.fast = fast
        self.slow = slow
        self.signal = signal

    def on_bar(self, bar) -> None:
        self.bars.append(bar)
        if len(self.bars) < self.slow:
            return

        macd_line, signal_line, hist = self.macd(self.fast, self.slow, self.signal)
        if hist > 0:
            self.buy()
        elif hist < 0:
            self.sell()
        else:
            self.flat()

from __future__ import annotations

from app.core.strategy import BaseStrategy


class RSI(BaseStrategy):
    def __init__(self, symbol: str, timeframe: str = "1h", period: int = 14, oversold: float = 30.0, overbought: float = 70.0) -> None:
        super().__init__(symbol, timeframe)
        self.period = period
        self.oversold = oversold
        self.overbought = overbought

    def on_bar(self, bar) -> None:
        self.bars.append(bar)
        if len(self.bars) < self.period + 1:
            return

        rsi_value = self.rsi(self.period)
        if rsi_value >= self.overbought:
            self.sell()
        elif rsi_value <= self.oversold:
            self.buy()
        else:
            self.flat()

from __future__ import annotations

from app.core.strategy import BaseStrategy


class RSI(BaseStrategy):
    def __init__(self, symbol: str, timeframe: str = "1h") -> None:
        super().__init__(symbol, timeframe)
        self.period = 14
        self.overbought = 70
        self.oversold = 30

    def on_bar(self, bar) -> None:
        if len(self.bars) < self.period:
            self.bars.append(bar)
            return
        self.bars.append(bar)
        del self.bars[0]
        closes = [entry.close for entry in self.bars]
        gains = [max(0, closes[i] - closes[i - 1]) for i in range(1, len(closes))]
        losses = [max(0, closes[i - 1] - closes[i]) for i in range(1, len(closes))]
        avg_gain = sum(gains[-self.period:]) / self.period
        avg_loss = sum(losses[-self.period:]) / self.period
        if avg_loss == 0:
            rsi = 100
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        if rsi > self.overbought:
            self.sell()
        elif rsi < self.oversold:
            self.buy()
        else:
            self.flat()

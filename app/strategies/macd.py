from __future__ import annotations

from app.core.strategy import BaseStrategy


class MACD(BaseStrategy):
    def __init__(self, symbol: str, timeframe: str = "1h") -> None:
        super().__init__(symbol, timeframe)

    def on_bar(self, bar) -> None:
        if len(self.bars) < 26:
            self.bars.append(bar)
            return
        self.bars.append(bar)
        del self.bars[0]
        closes = [entry.close for entry in self.bars]
        ema_fast = sum(closes[-12:]) / 12
        ema_slow = sum(closes[-26:]) / 26
        macd = ema_fast - ema_slow
        if macd > 0:
            self.buy()
        else:
            self.sell()

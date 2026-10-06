from __future__ import annotations

import pandas as pd


class MarketFeed:
    def __init__(self, source: str = "synthetic") -> None:
        self.source = source

    def load(self, symbol: str, days: int = 180, interval: str = "1h") -> pd.DataFrame:
        index = pd.date_range(end=pd.Timestamp.utcnow(), periods=days * 24, freq=interval)
        rng = pd.Series(range(len(index)), index=index)
        price = 100 + rng * 0.25
        data = pd.DataFrame(
            {
                "open": price,
                "high": price * 1.01,
                "low": price * 0.99,
                "close": price * 1.002,
                "volume": 1000 + rng * 5,
            },
            index=index,
        )
        data.index.name = "timestamp"
        return data


def create_market_feed(source: str = "synthetic") -> MarketFeed:
    return MarketFeed(source=source)

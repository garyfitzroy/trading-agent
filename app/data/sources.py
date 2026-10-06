from __future__ import annotations

from typing import Protocol

import pandas as pd


class DataSource(Protocol):
    def fetch(self, symbol: str, timeframe: str, periods: int) -> pd.DataFrame:
        ...


class SyntheticDataSource:
    def fetch(self, symbol: str, timeframe: str, periods: int) -> pd.DataFrame:
        index = pd.date_range(end=pd.Timestamp.utcnow(), periods=periods, freq=timeframe)
        base = 100.0
        price = base + (pd.Series(range(periods), index=index) * 0.5)
        return pd.DataFrame(
            {
                "open": price,
                "high": price * 1.02,
                "low": price * 0.98,
                "close": price * 1.01,
                "volume": 1000 + (pd.Series(range(periods), index=index) * 3),
            },
            index=index,
        )

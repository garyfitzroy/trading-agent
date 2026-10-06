from __future__ import annotations

import pandas as pd

from app.core.strategy import BaseStrategy


class BacktestEngine:
    def __init__(self, strategy_class: type[BaseStrategy], data: pd.DataFrame, initial_capital: float = 10_000.0) -> None:
        self.strategy_class = strategy_class
        self.data = data.copy()
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.position = 0
        self.trades: list[dict[str, float | str]] = []

    def run(self) -> dict[str, float | list[dict[str, float | str]]]:
        strategy = self.strategy_class(symbol="BTC/USD")
        for _, row in self.data.iterrows():
            bar = type("Bar", (), {
                "timestamp": str(row.name),
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": float(row["volume"]),
            })()
            strategy.on_bar(bar)
            if strategy.position == 1 and self.position == 0:
                self.cash -= row["close"]
                self.position = 1
                self.trades.append({"type": "buy", "price": float(row["close"]), "timestamp": str(row.name)})
            elif strategy.position == -1 and self.position == 1:
                self.cash += row["close"]
                self.position = 0
                self.trades.append({"type": "sell", "price": float(row["close"]), "timestamp": str(row.name)})

        return {
            "initial_capital": self.initial_capital,
            "final_cash": self.cash,
            "trades": self.trades,
        }

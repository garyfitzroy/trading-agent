from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Trade:
    symbol: str
    side: str
    quantity: float
    price: float
    timestamp: str
    pnl: float = 0.0


@dataclass
class Order:
    symbol: str
    side: str
    quantity: float
    price: float
    timestamp: str


@dataclass
class Portfolio:
    cash: float = 10_000.0
    currency: str = "USD"
    positions: dict[str, float] = field(default_factory=dict)
    trades: list[Trade] = field(default_factory=list)
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0

    @property
    def equity(self) -> float:
        return self.cash + self.position_value

    @property
    def position_value(self) -> float:
        return sum(self.positions.values())

    @property
    def pnl(self) -> float:
        return self.realized_pnl + self.unrealized_pnl


portfolio_manager = Portfolio()

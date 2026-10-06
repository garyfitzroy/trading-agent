from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RiskParameters:
    max_position_size: float = 0.2
    max_drawdown: float = 0.2
    stop_loss_pct: float = 0.05
    take_profit_pct: float = 0.1


@dataclass
class RiskManager:
    max_position_size: float = 0.2
    max_drawdown: float = 0.2
    stop_loss_pct: float = 0.05
    take_profit_pct: float = 0.1
    max_open_positions: int = 3
    current_drawdown: float = 0.0

    def __post_init__(self) -> None:
        self.params = RiskParameters(
            max_position_size=self.max_position_size,
            max_drawdown=self.max_drawdown,
            stop_loss_pct=self.stop_loss_pct,
            take_profit_pct=self.take_profit_pct,
        )

    def check_position_size(self, account_value: float, order_value: float) -> bool:
        return order_value <= account_value * self.max_position_size

    def check_drawdown(self, equity: float, peak_equity: float) -> bool:
        if peak_equity <= 0:
            return True
        self.current_drawdown = 1.0 - (equity / peak_equity)
        return self.current_drawdown <= self.max_drawdown

    def should_stop_loss(self, entry_price: float, current_price: float) -> bool:
        return (entry_price - current_price) / entry_price >= self.stop_loss_pct

    def should_take_profit(self, entry_price: float, current_price: float) -> bool:
        return (current_price - entry_price) / entry_price >= self.take_profit_pct

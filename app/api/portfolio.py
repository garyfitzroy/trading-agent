from __future__ import annotations

from fastapi import APIRouter

from app.core.portfolio import portfolio_manager

router = APIRouter(prefix="/portfolio", tags=["portfolio"])


@router.get("")
async def get_portfolio() -> dict[str, float | str]:
    return {
        "cash": portfolio_manager.cash,
        "equity": portfolio_manager.equity,
        "position_value": portfolio_manager.position_value,
        "currency": portfolio_manager.currency,
    }


@router.get("/metrics")
async def get_portfolio_metrics() -> dict[str, float]:
    return {
        "pnl": portfolio_manager.pnl,
        "realized_pnl": portfolio_manager.realized_pnl,
        "unrealized_pnl": portfolio_manager.unrealized_pnl,
        "position_count": len(portfolio_manager.positions),
    }

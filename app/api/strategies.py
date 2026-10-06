from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.models.schemas import StrategyCreate, StrategyResponse

router = APIRouter(prefix="/strategies", tags=["strategies"])

STRATEGIES: dict[str, StrategyResponse] = {}


@router.get("", response_model=list[StrategyResponse])
async def list_strategies() -> list[StrategyResponse]:
    return list(STRATEGIES.values())


@router.post("", response_model=StrategyResponse, status_code=201)
async def create_strategy(payload: StrategyCreate) -> StrategyResponse:
    strategy = StrategyResponse(
        id=f"strategy-{len(STRATEGIES) + 1}",
        name=payload.name,
        symbol=payload.symbol,
        timeframe=payload.timeframe,
        enabled=payload.enabled,
    )
    STRATEGIES[strategy.id] = strategy
    return strategy


@router.get("/{strategy_id}", response_model=StrategyResponse)
async def get_strategy(strategy_id: str) -> StrategyResponse:
    strategy = STRATEGIES.get(strategy_id)
    if strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.core.portfolio import portfolio_manager

router = APIRouter(prefix="/execution", tags=["execution"])

ACTIVE_EXECUTIONS: dict[str, bool] = {}


@router.post("/start")
async def start_execution(strategy: str, symbol: str) -> dict[str, str | bool]:
    ACTIVE_EXECUTIONS[strategy] = True
    return {"strategy": strategy, "symbol": symbol, "running": True}


@router.post("/stop")
async def stop_execution(strategy: str) -> dict[str, bool | str]:
    if strategy not in ACTIVE_EXECUTIONS:
        raise HTTPException(status_code=404, detail="Execution not found")
    ACTIVE_EXECUTIONS[strategy] = False
    return {"strategy": strategy, "running": False}


@router.get("/status")
async def get_execution_status(strategy: str) -> dict[str, bool | str]:
    return {"strategy": strategy, "running": ACTIVE_EXECUTIONS.get(strategy, False)}

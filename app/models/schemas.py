from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class StrategyCreate(BaseModel):
    name: str
    symbol: str
    timeframe: str = "1h"
    enabled: bool = True


class StrategyResponse(BaseModel):
    id: str
    name: str
    symbol: str
    timeframe: str
    enabled: bool = True


class ExecutionRequest(BaseModel):
    strategy: str
    symbol: str


class PortfolioSnapshot(BaseModel):
    cash: float
    equity: float
    position_value: float
    currency: str


class TradeResult(BaseModel):
    strategy: str
    symbol: str
    side: str
    quantity: float
    price: float
    status: str


class HealthResponse(BaseModel):
    status: str
    version: str = "0.1.0"
    environment: str = "development"


class Signal(BaseModel):
    symbol: str
    side: str
    confidence: float
    metadata: dict[str, Any] = {}

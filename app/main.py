from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.execution import router as execution_router
from app.api.portfolio import router as portfolio_router
from app.api.strategies import router as strategies_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Trading Agent",
        description="Algorithmic trading bot API with strategy execution and portfolio tracking",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(strategies_router)
    app.include_router(portfolio_router)
    app.include_router(execution_router)

    @app.get("/healthz")
    async def healthz() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()

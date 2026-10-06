# Trading Agent Architecture

## Overview

The application is structured around a few core responsibilities:

1. Data feed and market ingestion
2. Strategy evaluation and signal generation
3. Risk validation and portfolio management
4. Backtesting and paper trading execution
5. API exposure for analysis and manual orchestration

## Runtime flow

A typical flow starts with a market feed producing OHLCV bars for a symbol. The strategy engine consumes bars one at a time and emits long or short signals. The portfolio manager validates trade sizing, risk limits, and order execution. The backtest engine replays historical data to estimate performance. The FastAPI app exposes the portfolio and strategy state for monitoring.

## Core modules

- `app/core/strategy.py`: base strategy abstraction
- `app/core/backtest.py`: historical replay engine
- `app/core/portfolio.py`: position tracking and cash management
- `app/core/risk.py`: risk controls and drawdown checks
- `app/data/feed.py`: synthetic or external data access
- `app/strategies/`: strategy implementations such as RSI and MACD
- `app/api/`: HTTP routes for strategies and execution

## Risks and considerations

This repo intentionally keeps the architecture approachable and modular. In a production system, additional components such as exchange adapters, persistence, event queues, and monitoring should be added around this core structure.

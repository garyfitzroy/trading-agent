# Trading Agent

An algorithmic trading bot built with FastAPI, pandas, and a backtrader-style strategy engine. It provides a clean architecture for market data ingestion, trading strategy evaluation, backtesting, portfolio risk controls, and paper trading workflows.

## What it does

- Accepts bars or market data for a symbol
- Runs strategies with event-driven bar processing
- Tracks portfolio, cash, equity, and positions
- Evaluates risk metrics such as drawdown and position sizing
- Simulates historical trades through a backtesting engine
- Exposes a REST API for strategy control and reporting

## Stack

- Python 3.10+
- FastAPI for API layer
- pandas and numpy for market data processing
- Pydantic for validation and settings
- pytest for automated tests
- Backtrader-inspired strategy architecture

## Quick start

### 1) Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run the API server

```bash
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs

### 3) Run a backtest

```bash
python -m scripts.backtest --symbol BTC/USD --days 180 --strategy rsi
```

### 4) Run paper trading for a single symbol

```bash
python -m scripts.paper_trade --symbol BTC/USD --strategy rsi --interval 1h
```

## Repository layout

```text
app/               FastAPI app, domain logic, and strategies
scripts/           CLI entry points for backtesting and paper trading
tests/             automated tests for smoke, API, and strategy logic
docs/              architecture and strategy notes
```

## Example API routes

- `GET /healthz`
- `GET /strategies`
- `POST /strategies`
- `GET /portfolio`
- `POST /execution/start`
- `POST /execution/stop`

## Disclaimer

This project is for research and educational use only. Automated trading systems carry risk. Use proper research, simulation, and risk controls before any live execution.

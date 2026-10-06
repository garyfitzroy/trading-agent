from __future__ import annotations

import argparse

import pandas as pd

from app.core.backtest import BacktestEngine
from app.strategies.rsi import RSI


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a synthetic backtest for a trading strategy")
    parser.add_argument("--symbol", default="BTC/USD", help="Trading symbol")
    parser.add_argument("--days", type=int, default=180, help="Number of days of synthetic data")
    parser.add_argument("--strategy", default="rsi", choices=["rsi"], help="Strategy type")
    args = parser.parse_args()

    dates = pd.date_range(end=pd.Timestamp.utcnow(), periods=args.days * 24, freq="1h")
    price = 100 + (pd.Series(range(len(dates)), index=dates) * 0.25)
    data = pd.DataFrame(
        {"open": price, "high": price * 1.01, "low": price * 0.99, "close": price * 1.002, "volume": 1000},
        index=dates,
    )
    engine = BacktestEngine(RSI, data)
    result = engine.run()
    print(result)


if __name__ == "__main__":
    main()

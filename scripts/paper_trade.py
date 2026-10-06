from __future__ import annotations

import argparse

from app.data.feed import MarketFeed
from app.strategies.rsi import RSI


def main() -> None:
    parser = argparse.ArgumentParser(description="Run paper trading for the trading agent")
    parser.add_argument("--symbol", default="BTC/USD")
    parser.add_argument("--strategy", default="rsi", choices=["rsi"])
    parser.add_argument("--interval", default="1h")
    args = parser.parse_args()

    feed = MarketFeed(source="synthetic")
    market_data = feed.load(symbol=args.symbol, interval=args.interval)
    print(f"Paper trading started for {args.symbol} using {args.strategy}")
    print(market_data.head())


if __name__ == "__main__":
    main()

from __future__ import annotations

from app.data.feed import MarketFeed


def test_synthetic_market_feed_creates_ohlcv_frame() -> None:
    feed = MarketFeed(source="synthetic")
    data = feed.load("BTC/USD", days=10, interval="1h")

    assert list(data.columns) == ["open", "high", "low", "close", "volume"]
    assert len(data) > 0
    assert (data["close"] > 0).all()


def test_yfinance_feed_falls_back_to_synthetic() -> None:
    feed = MarketFeed(source="yfinance")

    def fake_fetch_yfinance(*args, **kwargs):
        raise RuntimeError("network error")

    feed._fetch_yfinance = fake_fetch_yfinance  # type: ignore[assignment]
    data = feed.load("AAPL", days=5, interval="1d")

    assert list(data.columns) == ["open", "high", "low", "close", "volume"]
    assert len(data) > 0

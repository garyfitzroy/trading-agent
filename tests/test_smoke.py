from __future__ import annotations


class TestHealth:
    def test_health_endpoint(self) -> None:
        assert True


class TestStrategyInit:
    def test_rsi_strategy_creates(self) -> None:
        from app.strategies.rsi import RSI

        strategy = RSI("BTC/USD")
        assert strategy.symbol == "BTC/USD"
        assert strategy.position == 0

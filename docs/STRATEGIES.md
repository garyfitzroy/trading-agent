# Strategy Development Guide

## Strategy lifecycle

Each strategy inherits from `BaseStrategy` and implements the `on_bar` method. The method receives a bar object with `open`, `high`, `low`, `close`, `volume`, and a timestamp.

```python
from app.core.strategy import BaseStrategy


class MyStrategy(BaseStrategy):
    def on_bar(self, bar) -> None:
        # evaluate the bar
        if self.should_buy():
            self.buy()
        elif self.should_sell():
            self.sell()
        else:
            self.flat()
```

## Common strategy patterns

- Trend-following strategies
- Mean-reversion and oscillator-based strategies
- Breakout triggers
- Volatility filters and regime detection

## Risk controls

Every strategy should be paired with a risk manager that tracks:

- position sizing
- stop-loss thresholds
- take-profit thresholds
- maximum drawdown checks

## Backtesting

Historical performance should be measured before live execution. Run backtests over representative market data, then review profit, losses, drawdown, and trade counts.

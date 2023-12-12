from trading.strategies import TradingStrategy, VolatilityBreakoutStrategy


class StrategyFactory:
    @staticmethod
    def create(config: dict) -> TradingStrategy:
        strategy_type = config["type"]
        update_interval = config["interval"]

        if strategy_type == "VolatilityBreakout":
            return VolatilityBreakoutStrategy(20, 14, update_interval)

        raise ValueError("Unknown strategy type")

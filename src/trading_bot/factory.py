from trading_bot.trading_bot import TradingBot
from strategies import VolatilityBreakoutStrategy


class BotFactory:
    @staticmethod
    def create_bot(strategy_type: str):
        if strategy_type == "VolatilityBreakout":
            strategy = VolatilityBreakoutStrategy(20, 14)
        else:
            raise ValueError("Unknown strategy type")

        return TradingBot(strategy)

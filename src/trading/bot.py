from trading.states import BotState, WaitingState
from trading.strategies import StrategyManager, TradingStrategy
from trading.strategies.strategy_factory import StrategyFactory


class TradingBot:
    def __init__(self):
        self.strategy_manager = StrategyManager()
        self.state: BotState = WaitingState()

    def add_strategy(self, strategy: TradingStrategy):
        self.strategy_manager.add_strategy(strategy)

    def calculate_signals(self):
        self.strategy_manager.calculate_signals()

    def execute_trades(self):
        self.strategy_manager.get_combined_signal()
        # 조합된 시그널에 따라 매매 명령 실행

    def __str__(self):
        return (
            f"TradingBot(\n"
            f"  strategy_manager={self.strategy_manager},\n"
            f"  state={self.state}\n"
            f")"
        )


class BotFactory:
    @staticmethod
    def create_bot(strategy_configs: list[dict]) -> TradingBot:
        bot = TradingBot()

        for config in strategy_configs:
            strategy = StrategyFactory.create(config)
            bot.add_strategy(strategy)

        return bot

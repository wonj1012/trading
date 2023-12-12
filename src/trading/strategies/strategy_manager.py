from trading.strategies import TradingStrategy


class StrategyManager:
    def __init__(self):
        self.strategies: list[TradingStrategy] = []

    def add_strategy(self, strategy: TradingStrategy):
        self.strategies.append(strategy)

    def calculate_signals(self):
        for strategy in self.strategies:
            if strategy.is_time_to_update():
                strategy.calculate_signal()

    def get_combined_signal(self):
        # 전략들의 시그널을 조합
        pass

    def __str__(self):
        return f"StrategyManager(strategies={list(map(str, self.strategies))})"

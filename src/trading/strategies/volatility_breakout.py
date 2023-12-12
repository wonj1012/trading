from trading.strategies import TradingStrategy


class VolatilityBreakoutStrategy(TradingStrategy):
    def __init__(self, parameter1, parameter2, update_interval: int):
        super().__init__(update_interval)
        self.name = "Volatility Breakout"
        self.var = parameter1 + parameter2
        # 전략에 필요한 초기화

    def calculate_signal(self):
        # 시그널 계산 로직
        pass

    def get_signal(self):
        # 계산된 시그널 반환
        pass

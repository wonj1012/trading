from strategies.base_strategy import TradingStrategy
from indicators import MovingAverage, RSI


class VolatilityBreakoutStrategy(TradingStrategy):
    def __init__(self, moving_average_period: int, rsi_period: int):
        self.moving_average = MovingAverage(moving_average_period)
        self.rsi = RSI(rsi_period)

    def analyze_market_data(self, market_data):
        ma_value = self.moving_average.calculate(market_data)
        rsi_value = self.rsi.calculate(market_data)

        some_threshold = 0.5
        another_threshold = 0.3

        # 거래 신호 생성 로직
        if ma_value > some_threshold and rsi_value < another_threshold:
            return "Buy"

        if ma_value < some_threshold and rsi_value > another_threshold:
            return "Sell"

        return "Hold"

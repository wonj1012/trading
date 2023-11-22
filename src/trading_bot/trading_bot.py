from strategies import TradingStrategy
from trading_bot.states import WaitingState


class TradingBot:
    def __init__(self, strategy: TradingStrategy):
        self.strategy = strategy
        self.state = WaitingState()

    def update_market_data(self, market_data):
        # 시장 데이터 업데이트 및 상태 업데이트
        self.state.handle_market_data(market_data)

    def change_state(self, new_state):
        self.state = new_state

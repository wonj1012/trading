from trading_bot.states.bot_state import BotState


class WaitingState(BotState):
    def handle_market_data(self, market_data):
        # 대기 상태에서의 로직
        pass

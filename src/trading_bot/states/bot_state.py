from abc import ABC, abstractmethod


class BotState(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def handle_market_data(self, market_data):
        pass

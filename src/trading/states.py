from abc import ABC, abstractmethod


class BotState(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def handle_market_data(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}"


class WaitingState(BotState):
    def handle_market_data(self):
        pass

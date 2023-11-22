from abc import ABC, abstractmethod


class TradeCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

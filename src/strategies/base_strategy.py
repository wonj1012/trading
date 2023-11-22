from abc import ABC, abstractmethod


class TradingStrategy(ABC):
    @abstractmethod
    def analyze_market_data(self, market_data):
        pass

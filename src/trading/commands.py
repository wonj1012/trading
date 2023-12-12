from abc import ABC, abstractmethod

from models import Asset


class TradeCommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class BuyCommand(TradeCommand):
    def __init__(self, asset: Asset, quantity: float):
        self.asset = asset
        self.quantity = quantity

    def execute(self):
        print(f"Buying {self.quantity} of {self.asset.symbol}")


class SellCommand(TradeCommand):
    def __init__(self, asset: Asset, quantity: float):
        self.asset = asset
        self.quantity = quantity

    def execute(self):
        print(f"Selling {self.quantity} of {self.asset.symbol}")

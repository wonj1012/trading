from commands.trade import TradeCommand


class SellCommand(TradeCommand):
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity

    def execute(self):
        print(f"Selling {self.quantity} of {self.symbol}")

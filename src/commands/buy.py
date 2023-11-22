from commands.trade import TradeCommand


class BuyCommand(TradeCommand):
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity

    def execute(self):
        print(f"Buying {self.quantity} of {self.symbol}")

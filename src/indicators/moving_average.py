import pandas as pd
from indicators.indicator import Indicator


class MovingAverage(Indicator):
    def __init__(self, period):
        self.period = period

    def calculate(self, data: pd.DataFrame):
        return data["close"].rolling(window=self.period).mean()

from abc import ABC, abstractmethod

import pandas as pd


class Indicator(ABC):
    @abstractmethod
    def calculate(self, data):
        pass


class MovingAverage(Indicator):
    def __init__(self, period):
        self.period = period

    def calculate(self, data: pd.DataFrame):
        return data["close"].rolling(window=self.period).mean()


class RSI(Indicator):
    def __init__(self, period):
        self.period = period

    def calculate(self, data: pd.DataFrame):
        delta = data["close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.period).mean()

        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

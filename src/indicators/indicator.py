from abc import ABC, abstractmethod


class Indicator(ABC):
    @abstractmethod
    def calculate(self, data):
        pass

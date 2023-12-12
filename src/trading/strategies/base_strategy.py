import time
from abc import ABC, abstractmethod


class TradingStrategy(ABC):
    def __init__(self, update_interval: int):
        self.name = "None"
        self.update_interval = update_interval
        self.last_update_time = 0

    @abstractmethod
    def calculate_signal(self):
        pass

    @abstractmethod
    def get_signal(self):
        pass

    def is_time_to_update(self) -> bool:
        current_time = time.time()
        if current_time - self.last_update_time > self.update_interval:
            self.last_update_time = current_time
            return True
        return False

    def __str__(self):
        return f"{self.name}"

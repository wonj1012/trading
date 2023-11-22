import pandas as pd
from market_data.storage import DataStorage


class DataProvider:
    def __init__(self, storage: DataStorage):
        self.storage = storage

    def get_data(self, symbol, data_type) -> pd.DataFrame:
        # 저장된 데이터 반환 로직
        return self.storage.retrieve_data(symbol, data_type)

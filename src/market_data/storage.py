class DataStorage:
    def __init__(self):
        self.data_store = {}

    def store_data(self, data, symbol: str, data_type: str):
        # 데이터 저장 로직
        key = f"{symbol}_{data_type}"
        self.data_store[key] = data

    def retrieve_data(self, symbol: str, data_type: str):
        # 데이터 검색 로직
        key = f"{symbol}_{data_type}"
        return self.data_store.get(key, None)

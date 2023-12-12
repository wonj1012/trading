from data_manager.storage import DataStorageInterface
from models import Asset


class DataProvider:
    def __init__(self, storage: DataStorageInterface):
        self.storage = storage

    # def get_historical_data(self, asset: Asset):
    #     return self.storage.retrieve_data(
    #         model_class=Asset, identifier=asset.id
    #     ).historical_data
    #     )

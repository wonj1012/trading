from binance.client import Client

from binance_api.futures import BinanceFuturesData
from models import Asset
from utils.enums import AssetType, Exchange


class DataFetcher:
    def __init__(self, binance_client: Client):
        self.binance_futures = BinanceFuturesData(binance_client)
        self.live_data_streams = {}

    def get_historical_data(
        self, asset: Asset, interval: str, start_str: str, end_str: str | None = None
    ):
        if asset.exchange == Exchange.BINANCE.value:
            if asset.asset_type == AssetType.COINSPOT.value:
                return self.binance_futures.get_historical_data(
                    asset.symbol, interval, start_str, end_str
                )
            if asset.asset_type == AssetType.COINFUTURES.value:
                return self.binance_futures.get_historical_data(
                    asset.symbol, interval, start_str, end_str
                )
        raise NotImplementedError

    def subscribe_to_live_data(self, asset: Asset):
        if asset not in self.live_data_streams:
            self.live_data_streams[asset] = self.create_live_data_stream(asset)
        return self.live_data_streams[asset]

    def create_live_data_stream(self, asset: Asset) -> Asset:
        return asset

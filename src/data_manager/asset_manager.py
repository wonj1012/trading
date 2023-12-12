from typing import Type

import yaml

from models import Asset, CoinSpot, CoinFutures, Stock
from utils.enums import AssetType, Exchange
from utils.logger import with_logging


class AssetManager:
    def __init__(self):
        self.assets: dict[str, Asset] = {}

    @with_logging
    def add_asset(self, asset: Asset):
        """
        Add an asset to the manager.

        Args:
            asset (Asset): The asset to be added.
        """
        self.assets[asset.key] = asset

    @with_logging
    def create_asset(
        self,
        symbol: str,
        asset_type: AssetType,
        exchange: Exchange,
    ) -> Asset:
        """
        Create and add a new asset based on the given parameters.

        Args:
            symbol (str): The symbol of the asset.
            asset_type (AssetType): The type of the asset.
            exchange (Exchange): The exchange of the asset.

        Returns:
            Asset: The created asset.
        """
        asset_type_class_map: dict[AssetType, Type[Asset]] = {
            AssetType.COINSPOT: CoinSpot,
            AssetType.COINFUTURES: CoinFutures,
            AssetType.STOCK: Stock,
        }
        asset_class = asset_type_class_map[asset_type]
        asset = asset_class(
            symbol=symbol,
            exchange=exchange.value,
            asset_type=asset_type.value,
            key=f"{symbol}_{asset_type.value}_{exchange.value}",
        )
        self.add_asset(asset)
        return asset

    def load_assets_from_file(self, file_path: str | None = None):
        """
        Load assets from a specified YAML file and add them to the manager.

        Args:
            file_path (str | None): The path to the YAML file containing asset data.
                                    Defaults to 'assets.yaml' if not specified.
        """
        file_path = file_path or "assets.yaml"
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            for asset_data in data["assets"]:
                self.create_asset(
                    symbol=asset_data["symbol"],
                    asset_type=AssetType[asset_data["asset_type"]],
                    exchange=Exchange[asset_data["exchange"]],
                )

    def __getitem__(self, key: str) -> Asset:
        """
        Allow direct access to an asset using its key.

        Args:
            key (str): The key of the asset to retrieve.

        Returns:
            Asset: The asset associated with the given key.
        """
        return self.assets[key]

    def get_all_assets(self) -> list[Asset]:
        """
        Get a list of all assets managed.

        Returns:
            list[Asset]: A list of all assets.
        """
        return list(self.assets.values())

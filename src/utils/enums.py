from enum import Enum


class Exchange(Enum):
    BINANCE = "binance"


class AssetType(Enum):
    COINFUTURES = "coinfutures"
    COINSPOT = "coinspot"
    STOCK = "stock"

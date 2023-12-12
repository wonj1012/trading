from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, registry

from utils.enums import AssetType, Exchange

reg = registry()


@dataclass
class Asset(ABC):
    key: Mapped[str] = mapped_column(primary_key=True)
    # key = {symbol}_{asset_type}_{exchange}
    symbol: Mapped[str] = mapped_column()
    asset_type: Mapped[str] = mapped_column(Enum(AssetType))
    exchange: Mapped[str] = mapped_column(Enum(Exchange))

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_current_price(self) -> float:
        pass

    def to_dict(self) -> dict[str, str]:
        return {
            "key": self.key,
            "symbol": self.symbol,
            "asset_type": self.asset_type,  # Enum 타입일 경우 .value를 사용
            "exchange": self.exchange,  # Enum 타입일 경우 .value를 사용
        }


@reg.mapped_as_dataclass
class CoinSpot(Asset):
    __tablename__ = "coinspot"

    def get_value(self):
        return f"CoinSpot: {self.symbol}"

    def get_current_price(self) -> float:
        return 0


@reg.mapped_as_dataclass
class CoinFutures(Asset):
    __tablename__ = "coinfutures"

    def get_value(self):
        return f"CoinFutures: {self.symbol}"

    def get_current_price(self) -> float:
        return 0


@reg.mapped_as_dataclass
class Stock(Asset):
    __tablename__ = "stock"

    def get_value(self):
        return f"Stock: {self.symbol})"

    def get_current_price(self) -> float:
        return 0

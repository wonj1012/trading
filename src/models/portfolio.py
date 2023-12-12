from dataclasses import dataclass, field

from models import Asset


@dataclass
class HoldingInfo:
    position: str | None
    quantity: float
    average_purchase_price: float

    def get_current_value(self, current_price: float) -> float:
        return self.quantity * current_price


@dataclass
class Portfolio:
    assets: dict[Asset, HoldingInfo] = field(default_factory=dict)

    def update_asset(self, asset: Asset, quantity: float, purchase_price: float):
        self.assets[asset] = HoldingInfo(
            position=None, quantity=quantity, average_purchase_price=purchase_price
        )

    def get_current_total_value(self) -> float:
        total_value = 0
        for asset, holding_info in self.assets.items():
            total_value += holding_info.get_current_value(asset.get_current_price())
        return total_value

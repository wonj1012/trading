import os
from dotenv import load_dotenv

from data_manager import DataProvider, AssetManager
from data_manager.sqlite import SQLAlchemyDataStorage
from trading.bot import BotFactory


def main():
    sql_data_storage = SQLAlchemyDataStorage(db_url="sqlite+pysqlite:///data/db.sqlite")
    sql_data_storage.create_tables()

    asset_manager = AssetManager()
    asset_manager.load_assets_from_file(os.getenv("ASSETS_FILE_PATH"))

    for asset in asset_manager.get_all_assets():
        sql_data_storage.store_data(asset)

    # data_provider = DataProvider(DataStorage())
    # for asset in asset_manager.assets.values():
    #     data_provider.get_historical_data(asset)

    strategy_configs = [
        {"type": "VolatilityBreakout", "interval": "1m"},
        {"type": "VolatilityBreakout", "interval": "5m"},
        {"type": "VolatilityBreakout", "interval": "15m"},
        {"type": "VolatilityBreakout", "interval": "1h"},
        {"type": "VolatilityBreakout", "interval": "4h"},
    ]
    bot = BotFactory.create_bot(strategy_configs=strategy_configs)
    print(bot)


if __name__ == "__main__":
    load_dotenv()
    main()

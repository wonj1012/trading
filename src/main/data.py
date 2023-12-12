import os

from binance.client import Client
from dotenv import load_dotenv

from data_manager import DataFetcher, AssetManager


def main():
    asset_manager = AssetManager()
    asset_manager.load_assets_from_file(os.getenv("ASSETS_FILE_PATH"))

    for asset in asset_manager.assets.values():
        print(asset)

    data_fetcher = DataFetcher(
        binance_client=Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_SECRET_KEY"),
        )
    )

    data_list = []
    for asset in asset_manager.assets.values():
        data_list.append(
            data_fetcher.get_historical_data(
                asset, interval="1d", start_str="1 Nov, 2023", end_str="10 Nov, 2023"
            )
        )
    print(data_list)


if __name__ == "__main__":
    load_dotenv()
    main()

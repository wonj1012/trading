from trading_bot import BotFactory
from market_data import DataProvider, DataStorage


def main():
    data_provider = DataProvider(DataStorage())

    bot = BotFactory.create_bot("VolatilityBreakout")

    while True:
        # market_data = data_provider.get_data("BTCUSDT", "historical")
        # bot.update_market_data(market_data)
        print("Hello World!")
        print(bot)
        break


if __name__ == "__main__":
    main()

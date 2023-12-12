from models import Portfolio


class PortfolioManager:
    def __init__(self, data_fetcher):
        self.data_fetcher = data_fetcher
        self.portfolio = Portfolio()

    async def synchronize_portfolio(self):
        # portfolio_data = await self.data_fetcher.fetch_portfolio_data()
        # self.portfolio = portfolio_data
        pass

    def get_portfolio(self) -> Portfolio:
        return self.portfolio

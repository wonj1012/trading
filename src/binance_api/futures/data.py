from binance.client import Client


class BinanceFuturesData:
    def __init__(self, client: Client):
        self.client = client

    def get_historical_data(
        self,
        symbol: str,
        interval: str,
        start_str: str,
        end_str: str | None = None,
    ):
        """
        과거 데이터를 가져옵니다.
        :param symbol: 코인 티커 심볼, 예: 'BTCUSDT'
        :param interval: 데이터 간격, 예: '1d', '1h', '5m'
        :param start_str: 데이터 시작 시간, 예: '1 Jan, 2019'
        :param end_str: 데이터 종료 시간, 기본값은 현재 시간
        :return: 과거 데이터 리스트
        """
        candles = self.client.get_historical_klines(
            symbol, interval, start_str, end_str
        )
        return candles

    def get_realtime_data(self):
        """
        실시간 데이터 스트림을 생성합니다.
        :param symbol: 코인 티커 심볼, 예: 'BTCUSDT'
        :param callback: 데이터가 도착할 때마다 호출되는 콜백 함수
        """
        return

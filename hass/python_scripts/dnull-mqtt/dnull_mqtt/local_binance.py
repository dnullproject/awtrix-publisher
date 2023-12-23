from binance.spot import Spot


class Binance:
    def __init__(self, Config) -> None:
        self.config = Config
        self.client = Spot()
        # Get server timestamp
        # print(self.client.time())
        # Get klines of BTCUSDT at 1m interval
        # Get last 10 klines of BNBUSDT at 1h interval
        # print(self.client.klines("BNBUSDT", "1h", limit=10))

    def get_price(self, pair="BTCUSDT"):
        price = int(
            str(self.client.avg_price(pair)["price"]).split(".")[0]
        )  # TODO: ugly
        return f"{price:_}"

    # # API key/secret are required for user data endpoints
    # client = Spot(api_key='<api_key>', api_secret='<api_secret>')

    # # Get account and balance information
    # print(client.account())

    # # Post a new order
    # params = {
    #     'symbol': 'BTCUSDT',
    #     'side': 'SELL',
    #     'type': 'LIMIT',
    #     'timeInForce': 'GTC',
    #     'quantity': 0.002,
    #     'price': 9500
    # }

    # response = client.new_order(**params)
    # print(response)

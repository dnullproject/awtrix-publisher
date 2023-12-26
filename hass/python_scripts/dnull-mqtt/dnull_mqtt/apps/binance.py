from apps.app import App
from binance.spot import Spot
from config import Config

class AppBinance(App):
    def __init__(self, Config: Config) -> None:
        self.name = "binance"
        super().__init__(self.name, Config)
        self.client = Spot()


    def get_price(self, pair="BTCUSDT"):
        price = int(
            str(self.client.avg_price(pair)["price"]).split(".")[0]
        )  # TODO: ugly
        return f"{price:_}"

    def run(self):
        self.mqtt.publish(self.awtrix.message(f"BTC: {self.get_price()}"))


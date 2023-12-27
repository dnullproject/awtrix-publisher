from apps.app import App
from binance.spot import Spot
from config import Config


class AppBinance(App):
    def __init__(self, Config: Config) -> None:
        self.name = "binance"
        super().__init__(self.name, Config)
        self.client = Spot()
        self.awtrix.icon(self.name)

    def get_price(self, pair="BTCUSDT"):
        price = int(
            str(self.client.avg_price(pair)["price"]).split(".")[0]
        )  # TODO: ugly
        return f"{price:_}"

    def run(self):
        # message = [{"text": "BTC", "color": "Amber"}, {"text": self.get_price()}]
        message = f"--Amber::BTC-- {self.get_price()}"
        self.mqtt.publish(self.awtrix.message(message))


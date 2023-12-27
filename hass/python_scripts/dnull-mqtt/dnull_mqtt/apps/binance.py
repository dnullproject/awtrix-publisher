from apps.app import App
from binance.spot import Spot
from config import Config
from base_log import log

class AppBinance(App):
    def __init__(self, Config: Config) -> None:
        self.name = "binance"
        super().__init__(self.name, Config)
        self.client = Spot()
        self.awtrix.icon(self.name)
        

    def get_price(self, pair: str):
        price = int(
            str(self.client.avg_price(pair)["price"]).split(".")[0]
        )  # TODO: ugly
        return f"{price:_}"

    def run(self, pairs: list):
        messages = list()
        for pair in pairs:
            message = f"--White::{self.get_price(pair)}--"
            self.awtrix.icon(pair)
            messages.append(self.awtrix.message(message).copy())

            log.debug(f"binance: {pair} - {message}")
        log.debug(f"binance: {messages}")
        self.mqtt.publish(messages)

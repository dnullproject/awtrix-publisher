from mqtt import MQTT
from config import Config
from local_binance import Binance
from awtrix import Awtrix

class App:
    def __init__(self, name, Config, MQTT) -> None:
        self.name = name
        self.config = Config
        self.mqtt = MQTT
        self.mqtt.topic = self.name
        self.awtrix = Awtrix(scroll_speed=50)

class AppBinance(App):
    def __init__(self, Config, MQTT) -> None:
        self.name = "binance"
        super().__init__(self.name, Config, MQTT)
        self.binance = Binance(self.config)

    def run(self):
        self.mqtt.publish(
            self.awtrix.message(f"BTC: {self.binance.get_price()}")
        )

class AppBudget(App):
    def __init__(self, Config, MQTT) -> None:
        self.name = "budget"
        super().__init__(self.name, Config, MQTT)

    def run(self):
        self.mqtt.publish(
            self.awtrix.message(f"budget: TODO")
        )


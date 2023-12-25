from mqtt import MQTT
from config import Config
from local_binance import Binance
from awtrix import Awtrix

# from fatsecret import Fatsecret


class App:
    def __init__(self, name, Config) -> None:
        self.name = name
        self.config = Config
        self.mqtt = MQTT(self.config, self.name)
        self.awtrix = Awtrix(scroll_speed=50)


class AppBinance(App):
    def __init__(self, Config) -> None:
        self.name = "binance"
        super().__init__(self.name, Config)
        self.binance = Binance(self.config)

    def run(self):
        self.mqtt.publish(self.awtrix.message(f"BTC: {self.binance.get_price()}"))


class AppBudget(App):
    def __init__(self, Config) -> None:
        self.name = "budget"
        super().__init__(self.name, Config)

    def run(self):
        self.mqtt.publish(self.awtrix.message(f"budget: TODO"))


class AppNutrition(App):
    def __init__(self, Config) -> None:
        self.name = "nutrition"
        super().__init__(self.name, Config)

    def example(self):
        fs = Fatsecret(
            self.config.fatsecret_secret_key, self.config.fatsecret_client_id
        )
        auth_url = fs.get_authorize_url()

        print(
            f"Browse to the following URL in your browser to authorize access:\n{auth_url}"
        )

        pin = input("Enter the PIN provided by FatSecret: ")
        session_token = fs.authenticate(pin)

        foods = fs.foods_get_most_eaten()
        print("Most Eaten Food Results: {}".format(len(foods)))

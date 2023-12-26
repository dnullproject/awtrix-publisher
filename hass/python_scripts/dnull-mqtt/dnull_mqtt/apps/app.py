from mqtt import MQTT
from config import Config
from awtrix import Awtrix



class App:
    def __init__(self, name, Config) -> None:
        self.name = name
        self.config = Config
        self.mqtt = MQTT(self.config, self.name)
        self.awtrix = Awtrix(scroll_speed=50)

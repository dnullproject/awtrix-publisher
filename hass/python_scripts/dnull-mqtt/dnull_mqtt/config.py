# TODO: read from envs
import random


class Config:
    def __init__(self) -> None:
        self.broker = "192.168.0.205"
        self.port = int(1883)
        self.prefix = "awtrix/custom"
        self.client_id = f"python-mqtt-{random.randint(0, 1000)}"
        self.username = ""
        self.password = ""
        self.interval = int(30)
        self.binance_key = (
            ""
        )
        self.binance_secret = (
            ""
        )

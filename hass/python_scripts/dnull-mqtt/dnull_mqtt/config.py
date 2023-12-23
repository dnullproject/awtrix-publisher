# TODO: read from envs
import random


class Config:
    def __init__(self) -> None:
        self.broker = "192.168.0.205"
        self.port = int(1883)
        self.prefix = "awtrix/custom"
        self.username = "mqtt"
        self.password = "157345"
        self.interval = int(10)
        self.binance_key = (
            "MNzi7sLQyTLrcCOknvGkvI8N2FmqBe9vWhCuK9WLS1IZ3CN3mgOwX9BEjT6a1UBG"
        )
        self.binance_secret = (
            "XDSbzjKBjBOwGFwsZyvKwNA2gvy38DjOq6m5rokUXw7mEPqr47EIv5cdFA1argcn"
        )

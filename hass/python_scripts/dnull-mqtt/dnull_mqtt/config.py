from os import environ


class Config:
    def __init__(self) -> None:
        self.binance_key = environ.get("BINANCE_KEY")
        self.binance_secret = environ.get("BINANCE_SECRET")
        self.broker = environ.get("BROKER_HOST", "192.168.0.205")
        self.fatsecret_client_id = environ.get("FATSECRET_KEY")
        self.fatsecret_secret_key = environ.get("FATSECRET_SECRET")
        self.interval = int(10)
        self.password = environ.get("MQTT_PASSWORD")
        self.port = int(environ.get("BROKER_PORT", 1883))
        self.prefix = environ.get("MQTT_PREFIX", "awtrix/custom")
        self.username = environ.get("MQTT_USER")

from os import environ


class Config:
    def __init__(self) -> None:
        # Binance
        self.binance_key = environ.get("BINANCE_KEY")
        self.binance_secret = environ.get("BINANCE_SECRET")

        # MQTT
        self.mqtt_broker = environ.get("BROKER_HOST", "192.168.0.205")
        self.mqtt_port = int(environ.get("BROKER_PORT", 1883))
        self.mqtt_interval = int(10)
        self.mqtt_username = environ.get("MQTT_USER")
        self.mqtt_password = environ.get("MQTT_PASSWORD")
        self.mtqq_prefix = environ.get("MQTT_PREFIX", "awtrix/custom")
        # FatSecret
        self.fatsecret_client_id = environ.get("FATSECRET_KEY")
        self.fatsecret_secret_key = environ.get("FATSECRET_SECRET")
        # Notion
        self.notion_database_id = environ.get("NOTION_PAGE")
        self.notion_token = environ.get("NOTION_TOKEN")

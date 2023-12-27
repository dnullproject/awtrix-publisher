from os import environ


class Config:
    def __init__(self) -> None:
        # Binance
        self.binance_key = environ.get("BINANCE_KEY")
        self.binance_secret = environ.get("BINANCE_SECRET")
        self.binance_icon = "43722"

        # MQTT
        self.mqtt_broker = environ.get("BROKER_HOST", "192.168.0.205")
        self.mqtt_port = int(environ.get("BROKER_PORT", 1883))
        self.mqtt_interval = int(15)
        self.mqtt_username = environ.get("MQTT_USER")
        self.mqtt_password = environ.get("MQTT_PASSWORD")
        self.mtqq_prefix = environ.get("MQTT_PREFIX", "awtrix/custom")
        # FatSecret
        self.fatsecret_client_id = environ.get("FATSECRET_KEY")
        self.fatsecret_secret_key = environ.get("FATSECRET_SECRET")
        # Notion
        self.notion_database_id = environ.get("NOTION_PAGE")
        self.notion_token = environ.get("NOTION_TOKEN")
        self.notion_icon = "57587"
        self.notion_all_completed_icon = "47199"
        ## Notion icons
        self.notion_icons = {
            # 1/
            "11": "57635",
            "12": "57636",
            "13": "57637",
            "14": "57638",
            "15": "57639",
            # 2/
            "22": "57640",
            "23": "57641",
            "24": "57642",
            "25": "57643",
            # 3/
            "33": "57644",
            "34": "57645",
            "35": "57646",
            # 4/
            "44": "57647",
            "45": "57648",
            # 5/
            "55": "57649",
        }

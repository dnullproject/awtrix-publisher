from mqtt import MQTT
from config import Config
from app import AppBinance, AppBudget
import time

if __name__ == "__main__":
    config = Config()
    mqtt = MQTT(config)
    app_binance = AppBinance(config, mqtt)
    app_budget = AppBudget(config, mqtt)

    while True:
        app_binance.run()
        app_budget.run()

        time.sleep(config.interval)

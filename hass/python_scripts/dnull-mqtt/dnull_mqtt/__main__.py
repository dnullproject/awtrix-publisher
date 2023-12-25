from mqtt import MQTT
from config import Config
from app import AppBinance, AppBudget, AppNutrition
from app_notion import AppNotion
import time

if __name__ == "__main__":
    config = Config()
    app_binance = AppBinance(config)
    # app_budget = AppBudget(config)
    # app_nutrition = AppNutrition(config)
    app_notion = AppNotion(config)

    while True:
        app_binance.run()
        # app_budget.run()
        app_notion.run()

        time.sleep(config.mqtt_interval)

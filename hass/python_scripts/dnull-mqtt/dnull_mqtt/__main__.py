from mqtt import MQTT
from config import Config
from app import AppBinance, AppBudget, AppNutrition
import time

if __name__ == "__main__":
    config = Config()
    app_binance = AppBinance(config)
    app_budget = AppBudget(config)
    # app_nutrition = AppNutrition(config)

    while True:
        app_binance.run()
        app_budget.run()

        time.sleep(config.interval)

# Lib: https://github.com/ramnes/notion-sdk-py
# Examples of usage: https://github.com/kris-hansen/notion-cli/blob/main/notioncli/cli.py#L26
# Database filters: https://developers.notion.com/reference/post-database-query-filter

from app import App
from notion_client import Client
from config import Config
from pprint import pprint
import json


class AppNotion(App):
    def __init__(self, Config: Config) -> None:
        self.name = "notion"
        super().__init__(self.name, Config)

        self.notion = Client(auth=self.config.notion_token)
        # self.page = self.notion.pages.retrieve(self.config.notion_page)
        my_page = self.notion.databases.query(
            **{
                "database_id": self.config.notion_page,
                "filter": {
                    "property": "SP",
                    "number": {
                        "equals": 10,
                    },
                },
            }
        )
        with open("data.json", "w") as f:
            json.dump(my_page, f)
        pprint(my_page)

        # list_users_response = self.notion.users.list()
        # pprint(list_users_response)

    def run(self):
        self.mqtt.publish(self.awtrix.message(f"TODO:"))

# Lib: https://github.com/ramnes/notion-sdk-py
# Examples of usage: https://github.com/kris-hansen/notion-cli/blob/main/notioncli/cli.py#L26
# Database filters: https://developers.notion.com/reference/post-database-query-filter

from apps.app import App
from notion_client import Client
from config import Config
from datetime import datetime, timedelta
import httpx


class AppNotion(App):
    def __init__(self, Config: Config) -> None:
        self.name = "notion"
        super().__init__(self.name, Config)
        self.awtrix.settings["duration"] = 0
        self.awtrix.settings["icon"] = self.awtrix.icons.get(self.name)
        self.notion = Client(auth=self.config.notion_token)

    def _get_todays_todo(self):
        current_datetime_utc2 = datetime.utcnow() + timedelta(hours=2)
        today = current_datetime_utc2.date()
        # print(f"TODAY is {today}")

        database = self.notion.databases.query(
            **{
                "database_id": self.config.notion_database_id,
                "filter": {
                    # "and": [
                    # {
                    "property": "Time",
                    "date": {
                        "this_week": {},
                    },
                    # },
                    # {
                    #     "or": [
                    #         {
                    #             "property": "Status",
                    #             "status": {
                    #                 "equals": "Backlog",
                    #             },
                    #         },
                    #         {
                    #             "property": "Status",
                    #             "status": {
                    #                 "equals": "Soon",
                    #             },
                    #         },
                    #         {
                    #             "property": "Status",
                    #             "status": {
                    #                 "equals": "In progress",
                    #             },
                    #         }
                    #     ]
                    # },
                    # ],
                },
                "sorts": [{"property": "Time", "direction": "ascending"}],
            }
        )
        # Time:
        # '.results[0].properties.Time.date.start'
        # Status:
        # '.results[0].properties.Status.status.name'

        todays_todo = list()
        if not database["results"]:
            print("No TODOs")
        else:
            for item in database["results"]:
                name = item["properties"]["Name"]["title"][0]["plain_text"]
                status = item["properties"]["Status"]["status"]["name"]
                time = datetime.fromisoformat(
                    item["properties"]["Time"]["date"]["start"]
                ).date()

                if time == today:
                    todays_todo.append({"name": name, "time": time, "status": status})

        return todays_todo

    def _set_scroll_speed(self, text: str):
        # TODO: use formula instead of hardcode
        symbols = len(text)
        if symbols <= 15:
            self.awtrix.settings["scroll_speed"] = 50
        elif symbols > 15 and symbols <= 25:
            self.awtrix.settings["scroll_speed"] = 75
        else:
            self.awtrix.settings["scroll_speed"] = 100

    def _set_icon(self, todo_tasks_no, all_tasks_no):
        if todo_tasks_no == 0 or all_tasks_no == 0:
            self.awtrix.icon("green_checkmark")
        else:
            icon_no = str(todo_tasks_no) + str(all_tasks_no)
            self.awtrix.icon(icon_no)

    def run(self):
        try:
            tasks = self._get_todays_todo()
        except httpx.HTTPStatusError as e:
            print(f"Issue with Notion API: {e}")
            self.awtrix.icon("error")
            self.mqtt.publish(self.awtrix.message("--Red::connection error--"))
        else:
            task_names = str()
            todo_tasks_no = 0
            all_tasks_no = len(tasks)
            if all_tasks_no == 0:
                message = "No tasks"
            else:
                todo_statuses = ["Backlog", "Soon", "In progress"]
                todo = list()
                for task in tasks:
                    if task["status"] in todo_statuses:
                        todo.append(task["name"])
                todo_tasks_no = len(todo)
                if todo_tasks_no == 0:
                    message = f"{all_tasks_no} completed"
                else:
                    task_names = ", ".join(todo)
                    message = f"--Green::{task_names}--"

            self._set_icon(todo_tasks_no, all_tasks_no)
            self._set_scroll_speed(task_names)
            self.mqtt.publish(self.awtrix.message(message))

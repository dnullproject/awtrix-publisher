from dnull_mqtt.config import Config
from dnull_mqtt.apps.notion import TestAppNotion


mock_tasks = [
    {
        "name": "Work: Prod Deploy",
        "time": "2024, 2, 6",
        "status": "Ready",
    },
    {
        "name": "Health: Rollouts",
        "time": "2024, 2, 6",
        "status": "Ready",
    },
]

mock_result = "{'autoscale': True, 'background': None, 'bar': None, 'blinkText': None, 'center': True, 'color': None, 'duration': 0, 'fadeText': None, 'gradient': None, 'hold': False, 'icon': '57640', 'lifetime': 0, 'lifetimeMode': 0, 'line': None, 'loopSound': False, 'noScroll': False, 'pos': None, 'progress': -1, 'progressBC': -1, 'progressC': -1, 'pushIcon': 0, 'rainbow': False, 'repeat': 0, 'rtttl': None, 'scrollSpeed': 100, 'sound': None, 'stack': True, 'text': [{'t': 'Prod Deploy, Health: Rollouts', 'c': 'FFFFFF'}], 'textCase': 1, 'textOffset': 0, 'topText': False, 'wakeup': False}"

config = Config()
config.notion_delete_prefixes = "Work:"

app_notion = TestAppNotion(config)


def test_notion():
    assert mock_result == app_notion.test(tasks=mock_tasks)

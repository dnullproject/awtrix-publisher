from paho.mqtt import client as mqtt_client
from config import Config
import json


class MQTT:
    def __init__(self, Config, topic='notify') -> None:
        self.config = Config
        self.client = self.connect()
        self.topic = f"{self.config.prefix}/{topic}"

    def connect(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print(f"Connected to MQTT Broker: {self.topic}")
            else:
                print(f"Failed to connect {self.topic}, return code %d\n", rc)

        # Set Connecting Client ID
        client = mqtt_client.Client(self.config.client_id)
        client.username_pw_set(self.config.username, self.config.password)
        client.on_connect = on_connect
        client.connect(self.config.broker, self.config.port)
        return client

    def publish(self, msg):
        result = self.client.publish(self.topic, json.dumps(msg))
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"{self.topic}: publish {msg}")
        else:
            print(f"Failed to send message to topic {self.topic}")

    def run(self):
        self.client.loop_start()

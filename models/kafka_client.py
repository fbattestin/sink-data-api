from confluent_kafka import Producer
import json
from .sink import SinkClient


class KafkaClient(SinkClient):
    def __init__(self, **kwargs):
        self.producer = Producer({'bootstrap.servers': kwargs.get('brokers')})
        self.topic = kwargs.get('topic')

    def send_message(self, message, key):
        self.producer.produce(self.topic, key=key, value=json.dumps(message))
        self.producer.flush()

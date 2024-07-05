import requests
from models.s3_client import S3Client
from models.kafka_client import KafkaClient


def get_sink_client(sink_type, **kwargs):
    dispatch_table = {
        's3': S3Client,
        'kafka': KafkaClient
    }
    if sink_type not in dispatch_table:
        raise ValueError(f"Invalid SINK_TYPE: {sink_type}. Choose 's3' or 'kafka'.")
    return dispatch_table[sink_type](**kwargs)


SINK_TYPE = 'kafka'  # or 's3'
SINK_CONFIG = {
    's3': {'bucket_name': 'your-bucket-name'},
    'kafka': {'brokers': 'your-kafka-broker', 'topic': 'your-topic'}
}

sink_client = get_sink_client(SINK_TYPE, **SINK_CONFIG[SINK_TYPE])


def confirm_subscription(subscribe_url):
    response = requests.get(subscribe_url)
    if response.status_code == 200:
        print("Subscription confirmed successfully.")
    else:
        print(f"Failed to confirm subscription: {response.status_code}")


def process_sns_message(headers, message):
    sns_message_type = headers.get('x-amz-sns-message-type')

    if sns_message_type == 'SubscriptionConfirmation':
        subscribe_url = message['SubscribeURL']
        print(f"Subscription confirmation URL: {subscribe_url}")
        confirm_subscription(subscribe_url)
    elif sns_message_type == 'Notification':
        notification_message = message['Message']
        print(f"Received message: {notification_message}")

        # Store the message using the selected sink client
        key = f"notifications/{message['MessageId']}.json"
        response = sink_client.send_message(message, key)
        print(f"Message stored with response: {response}")

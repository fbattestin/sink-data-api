import boto3
import json
from .sink import SinkClient


class S3Client(SinkClient):
    def __init__(self, **kwargs):
        self.s3 = boto3.client('s3')
        self.bucket_name = kwargs.get('bucket_name')

    def send_message(self, message, key):
        response = self.s3.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=json.dumps(message)
        )
        return response

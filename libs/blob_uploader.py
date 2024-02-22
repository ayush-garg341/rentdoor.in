from abc import ABC, abstractmethod
import os
import boto3


class BlobUploader(ABC):

    @abstractmethod
    def create_session(self):
        pass

    @abstractmethod
    def upload_file(self):
        pass


class DigitalOceanUploader(BlobUploader):

    def __init__(self):
        self.access_key = os.getenv("S3_ACCESS_KEY")
        self.secret_key = os.getenv("S3_SECRET_KEY")
        self.region = os.getenv("S3_REGION")
        self.endpoint_url = os.getenv("S3_ENDPOINT")

    def create_session(self):
        session = boto3.session.Session()
        client = session.client(
            "s3",
            region_name=self.region,
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )
        return client

    def upload_file(self, file, filename, bucket_name, is_public):
        client = self.create_session()

        client.put_object(
            Bucket=bucket_name, Key=filename, Body=file, ACL="public-read"
        )
        return "{}/{}/{}".format(self.endpoint_url, bucket_name, file)

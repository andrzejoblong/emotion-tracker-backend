import boto3
from app.core.config import settings

s3_client = boto3.client('s3', region_name=settings.AWS_REGION)

def upload_file_to_s3(file, bucket_name, object_name):
    try:
        s3_client.upload_fileobj(file, bucket_name, object_name)
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise

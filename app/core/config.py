import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    AWS_S3_BUCKET: str = os.getenv("AWS_S3_BUCKET", "emotion-tracker-bucket")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/emotion_tracker")
    COGNITO_USER_POOL_ID: str = os.getenv("COGNITO_USER_POOL_ID")
    COGNITO_APP_CLIENT_ID: str = os.getenv("COGNITO_APP_CLIENT_ID")
    COGNITO_APP_CLIENT_SECRET: str = os.getenv("COGNITO_APP_CLIENT_SECRET")

settings = Settings()

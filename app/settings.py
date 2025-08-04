
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    VONAGE_API_KEY: str
    VONAGE_API_SECRET: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    OTP_EXPIRE_SECONDS: int = 300

    class Config:
        env_file = ".env"

settings = Settings()

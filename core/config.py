from pydantic import AnyHttpUrl, SecretStr, StrictStr
from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Crypto Price Watcher API"
    API_V1_STR: str = "/api/v1"

    COINGECKO_API_URL: AnyHttpUrl = "https://api.coingecko.com/api/v3"
    COINGECKO_API_KEY: SecretStr
    BINANCE_API_KEY: Optional[SecretStr] = None
    BINANCE_API_SECRET: Optional[SecretStr] = None
    KRAKEN_API_KEY: Optional[SecretStr] = None
    KRAKEN_API_SECRET: Optional[SecretStr] = None
    DEFAULT_VS_CURRENCY: StrictStr = "usd"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
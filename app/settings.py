from datetime import datetime

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # General settings
    ENVIRONMENT: str = "development"
    SERVICE: str = "no-mcp"
    DEPLOYMENT_DATE: str = datetime.now().strftime("%Y-%m-%d")

    # Logging
    LOG_LEVEL: str = "info"

    # NaaS
    NO_BASE_URL: HttpUrl = "https://naas.isalman.dev"

    # API Configuration
    API_PORT: int = 8000
    API_HOST: str = "0.0.0.0"
    API_WORKERS: int = 4

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


# Create a global settings instance
settings = Settings()

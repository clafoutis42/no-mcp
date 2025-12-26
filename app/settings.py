from datetime import datetime

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # General settings
    ENVIRONMENT: str = "development"
    SERVICE: str = "No MCP"
    DEPLOYMENT_DATE: str = datetime.now().strftime("%Y-%m-%d")

    # Logging
    LOG_LEVEL: str = "info"

    # NaaS
    NO_BASE_URL: HttpUrl = "https://naas.isalman.dev"

    # Server Config
    MCP_TRANSPORT: str = "stdio"

    MCP_HTTP_HOST: str = "0.0.0.0"
    MCP_HTTP_PORT: int = 8000
    MCP_HTTP_PATH: str = "/mcp"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


# Create a global settings instance
settings = Settings()

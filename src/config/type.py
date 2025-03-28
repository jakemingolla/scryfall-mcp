import os

from pydantic_settings import BaseSettings, SettingsConfigDict

env_file_path = os.getenv("ENV_FILE_PATH", ".env")


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(env_file_path).strip(),
        env_file_encoding="utf-8",
        extra="ignore",
        hide_input_in_errors=True,
    )

    ENVIRONMENT: str = "development"
    "The Robin environment the application is running in."
    LOG_LEVEL: str = "DEBUG"

    SCRYFALL_API_BASE_URL: str = "https://api.scryfall.com"

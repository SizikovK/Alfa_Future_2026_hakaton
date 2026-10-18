from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[3] / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: str = "development"
    log_level: Literal["critical", "error", "warning", "info", "debug"] = "info"
    llm_api_key: SecretStr = SecretStr("")
    llm_model: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Trading Agent"
    environment: str = "development"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    log_level: str = "INFO"
    initial_capital: float = 10_000.0
    max_position_size: float = 0.2
    max_drawdown: float = 0.2
    base_currency: str = "USD"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()

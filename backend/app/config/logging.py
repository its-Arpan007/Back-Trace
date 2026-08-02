from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"  # json or text

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


logging_settings = LoggingSettings()

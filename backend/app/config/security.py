from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class SecuritySettings(BaseSettings):
    ALLOWED_HOSTS: List[str] = ["*"]
    ENABLE_CSRF_PROTECTION: bool = True
    ENABLE_RATE_LIMITING: bool = True
    RATE_LIMIT_PER_MINUTE: int = 100

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


security_settings = SecuritySettings()

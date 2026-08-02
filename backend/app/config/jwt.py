from pydantic_settings import BaseSettings, SettingsConfigDict


class JWTSettings(BaseSettings):
    SECRET_KEY: str = "backtrace_super_secret_key_change_in_production_environment_32chars_min"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


jwt_settings = JWTSettings()

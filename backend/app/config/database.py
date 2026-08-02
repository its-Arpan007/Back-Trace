from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "backtrace_user"
    POSTGRES_PASSWORD: str = "backtrace_password_secure"
    POSTGRES_DB: str = "backtrace_db"
    DATABASE_URL: str = (
        "postgresql+asyncpg://backtrace_user:backtrace_password_secure@localhost:5432/backtrace_db"
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


database_settings = DatabaseSettings()

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str
    DATABASE_URL: str
    HR_WEBHOOK_API_KEY: SecretStr
    IDENTITY_PROVIDER: str
    GITHUB_SIMULATE: bool
    GITHUB_TOKEN: SecretStr | None = None
    GITHUB_ORG: str | None = None
    REDIS_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )


settings = Settings()  # type: ignore

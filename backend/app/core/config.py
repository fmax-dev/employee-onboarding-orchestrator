from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str
    HR_WEBHOOK_API_KEY: str
    IDENTITY_PROVIDER: str
    GITHUB_SIMULATE: bool
    GITHUB_TOKEN: str
    GITHUB_ORG: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore"
    )

settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "boilerplate"
    async_database_url: str = "postgresql+asyncpg://dev:dev@localhost:5432/app"


settings = Settings()

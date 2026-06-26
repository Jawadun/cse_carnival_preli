from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = Field("development", env="APP_ENV")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    gemini_api_key: str | None = Field(None, env="GEMINI_API_KEY")
    gemini_model: str = Field("gemini-2.5-flash", env="GEMINI_MODEL")
    gemini_timeout: int = Field(30, env="GEMINI_TIMEOUT")
    gemini_retries: int = Field(3, env="GEMINI_RETRIES")

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

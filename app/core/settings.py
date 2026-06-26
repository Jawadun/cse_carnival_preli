from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = Field("development", env="APP_ENV")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    gemini_api_key: str = Field(..., env="GEMINI_API_KEY")
    gemini_model: str = Field("gemini-2.5-flash", env="GEMINI_MODEL")
    gemini_timeout: int = Field(30, env="GEMINI_TIMEOUT")
    retry_attempts: int = Field(3, env="RETRY_ATTEMPTS")
    retry_backoff: int = Field(2, env="RETRY_BACKOFF")

    class Config:
        env_file = ".env"
        validate_assignment = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

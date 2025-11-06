import os
from typing_extensions import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    ENVIRONMENT: Literal["development", "production"] = Field("development", env="ENVIRONMENT")  # type: ignore

    # AWS Settings
    AWS_REGION: str = Field("us-east-2", env="AWS_REGION")  # type: ignore
    AWS_ACCESS_KEY_ID: str | None = Field(None, env="AWS_ACCESS_KEY_ID")  # type: ignore
    AWS_SECRET_ACCESS_KEY: str | None = Field(None, env="AWS_SECRET_ACCESS_KEY")  # type: ignore

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()  # type: ignore

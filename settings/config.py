from pydantic import AnyUrl, Field, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    rtsp_url: AnyUrl | None = Field(validation_alias="RTSP_URL", default=None)
    video_path: FilePath | None = Field(
        validation_alias="VIDEO_PATH", default=None
    )
    config_name_file: str = Field(validation_alias="CONFIG_NAME")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

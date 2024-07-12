from typing import Annotated

from pydantic import Field, FilePath, UrlConstraints
from pydantic_core import Url
from pydantic_settings import BaseSettings, SettingsConfigDict

RtspUrl = Annotated[
    Url,
    UrlConstraints(
        allowed_schemes=["rtsp"],
        default_host="localhost",
        default_port=554,
        default_path="/1",
    ),
]


class Settings(BaseSettings):
    rtsp_url: RtspUrl | None = Field(validation_alias="RTSP_URL", default=None)
    video_path: FilePath | None = Field(
        validation_alias="VIDEO_PATH", default=None
    )
    config_name_file: str = Field(validation_alias="CONFIG_NAME")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


settings = Settings()

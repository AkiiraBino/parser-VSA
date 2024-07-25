import os
from datetime import datetime
from pathlib import PosixPath

import cv2
from loguru import logger
from pydantic import FilePath
from pydantic_core import Url

from settings.config import RtspUrl


def parse(
    set_images_path: str,
    set_labels_path: str,
    frame_limit: int,
    uri: RtspUrl | str | FilePath,
    file_format: str = ".png",
) -> None:
    capture = cv2.VideoCapture(str(uri))
    num_of_saved: int = 0

    if not capture.isOpened():
        logger.error("Error opened capture")
        return None

    status: bool
    frame: cv2.typing.MatLike
    logger.info("Capture is OK")

    while True:
        status, frame = capture.read()

        if not status:
            logger.error("Status false")
            return None

        if num_of_saved >= frame_limit:
            break

        name: str = "_".join(
            [(_get_filename(uri)), str(datetime.now()), file_format]
        ).replace("/", "-")

        images_path: str = os.path.join(set_images_path, name)
        labels_path: str = os.path.join(
            set_labels_path, name.replace("png", "txt")
        )

        num_of_saved += 1
        cv2.imwrite(images_path, frame)
        open(labels_path, "w").close()
        logger.info(f"Saving {name} along the path {images_path}")

    capture.release()


def _get_filename(uri: RtspUrl | FilePath) -> str | None:
    if type(uri) is PosixPath:
        return uri.stem
    if type(uri) is Url:
        return uri.host
    raise TypeError(f"Invalid uri: {uri}")

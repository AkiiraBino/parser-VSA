import os
from datetime import datetime

import cv2
from loguru import logger
from pydantic import AnyUrl


def parsing(
    dataset_path, uri: str | AnyUrl, file_format=".png", frame_limit=100
):
    capture = cv2.VideoCapture(uri)
    num_of_saved = 0

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

        if num_of_saved <= frame_limit:
            name = "_".join([uri, datetime.now(), file_format])
            path = os.path.join(dataset_path, name)
            num_of_saved += 1
            cv2.imwrite(path, frame)

            logger.info(f"Saving {name} along the path {path}")

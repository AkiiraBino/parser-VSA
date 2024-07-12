import os
from datetime import datetime

import cv2
from loguru import logger


def parse(
    set_images_path: str,
    set_labels_path: str,
    uri: str,
    file_format: str = ".png",
    frame_limit: int = 100,
) -> None:
    capture = cv2.VideoCapture(uri)
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

        name: str = "_".join([uri, str(datetime.now()), file_format]).replace(
            "/", "-"
        )

        images_path: str = os.path.join(set_images_path, name)
        labels_path: str = os.path.join(
            set_labels_path, name.replace("png", "txt")
        )

        num_of_saved += 1
        cv2.imwrite(images_path, frame)
        open(labels_path, "w").close()
        logger.info(f"Saving {name} along the path {images_path}")

    capture.release()

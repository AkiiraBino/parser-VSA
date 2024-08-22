import os
from venv import logger

from settings.config import settings
from src.models import Dataset
from src.parsing import parse
from src.utils import (
    create_folders,
    get_images_paths,
    get_labels_paths,
    parse_yaml,
)

root_dir = os.getcwd()
if __name__ == "__main__":
    config_path = os.path.join(root_dir, settings.config_name_file)
    config = parse_yaml(config_path)
    dataset = Dataset.model_validate(config.get("datasets"))

    create_folders(dataset)

    images_paths: dict[str, str] = get_images_paths(dataset)
    labels_paths: dict[str, str] = get_labels_paths(dataset)

    uris = []

    if settings.video_path:
        uris.append(settings.video_path)

    if settings.rtsp_url:
        uris.append(settings.rtsp_url)

    if settings.folder_with_video:
        uris.extend(settings.folder_with_video.glob("*.mp4"))
    for _set in dataset.sets:
        logger.info(f"Save set {_set}")
        for uri in uris:
            parse(
                set_images_path=images_paths[_set.folder_name],
                set_labels_path=labels_paths[_set.folder_name],
                frame_limit=_set.number,
                uri=uri,
            )

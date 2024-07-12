import os

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
    parse(images_paths["train"], labels_paths["train"], str(settings.rtsp_url))

import os

import yaml
from loguru import logger

from src.models import Dataset


def parse_yaml(path: str) -> dict:
    with open(path) as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logger.error("YAML parse error")
            raise e
    return config


def create_folders(dataset: Dataset) -> None:
    root_path: str = os.path.join(os.getcwd(), dataset.root)
    create_dir_if_not_exists(root_path)
    for _set in dataset.sets:
        set_dir_path: str = os.path.join(root_path, _set.folder_name)
        create_dir_if_not_exists(set_dir_path)

        images_path: str = os.path.join(set_dir_path, dataset.images)
        labels_path: str = os.path.join(set_dir_path, dataset.labels)
        create_dir_if_not_exists(images_path)
        create_dir_if_not_exists(labels_path)


def create_dir_if_not_exists(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)
        logger.info(f"Creating `{path} dir`")


def get_images_paths(dataset: Dataset) -> dict[str, str]:
    return {
        _set._folder_name: os.path.join(_set.path, dataset.images)
        for _set in dataset.sets
    }


def get_labels_paths(dataset: Dataset) -> dict[str, str]:
    return {
        _set._folder_name: os.path.join(_set.path, dataset.labels)
        for _set in dataset.sets
    }

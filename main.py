import os

from settings.config import settings
from src.models import Dataset
from src.utils import create_folders, parse_yaml

root_dir = os.getcwd()


if __name__ == "__main__":
    config_path = os.path.join(root_dir, settings.config_name_file)
    config = parse_yaml(config_path)
    dataset = Dataset.model_validate(config.get("datasets"))

    create_folders(dataset)

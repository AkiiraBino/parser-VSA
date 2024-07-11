
import os

from settings.config import Settings
from src.models import Dataset
from src.utils import parse_yaml


root_dir = os.getcwd()





if __name__ == "__main__": 
    settings = Settings()
    config_path = os.path.join(root_dir, settings.config_name_file)
    config = parse_yaml(config_path)
    print(config)
    dataset = Dataset.model_validate(config)
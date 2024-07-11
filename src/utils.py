import yaml
from loguru import logger

def parse_yaml(path: str):
    with open(path, "r") as stream:
        try:
            config = yaml.safe_load(stream)

        except yaml.YAMLError:
            logger.error("YAML parse error")
            raise yaml.YAMLError

    return config
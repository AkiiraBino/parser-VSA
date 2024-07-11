import yaml
from loguru import logger


def parse_yaml(path: str):
    with open(path) as stream:
        try:
            config = yaml.safe_load(stream)

        except yaml.YAMLError as e:
            logger.error("YAML parse error")
            raise e

    return config

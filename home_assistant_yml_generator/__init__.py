
import json
import logging.config

def setup_logging():
    with open('logging_config.json', 'r') as config_file:
        config = json.load(config_file)
    logging.config.dictConfig(config)

setup_logging()
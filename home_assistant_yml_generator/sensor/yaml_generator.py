from jinja2 import Environment, FileSystemLoader, select_autoescape

import logging
import json
from os import listdir, remove, getcwd
from os.path import isfile, join
from glob import glob

logger = logging.getLogger(__name__)

def generateYAML():
    logger.info("generateTempSensor")
    clearDir()
    env = Environment(
        loader=FileSystemLoader("templates"), autoescape=select_autoescape()
    )
    device_path = "areas/"
    deviece_configs = [
        f
        for f in listdir(device_path)
        if isfile(join(device_path, f)) and not f.startswith(".")
    ]
    logger.info(f"Number of Configurationfiles: {len(deviece_configs)}")
    for device_config in deviece_configs:
        logger.info(f"Configurationfile: {device_config}")
        with open(join(device_path, device_config)) as json_data:
            area = json.load(json_data)
            logger.info(
                f"Number of Devices for {device_config}: {len(area["devices"])}"
            )
            for device in area["devices"]:
                logger.info(f"{device['device_name']}: {device['template']}")
                device["suggested_area"] = area["suggested_area"]
                yml_conf = generateConfigs(env, device)
                filename = (
                    f"{area["suggested_area"]} {device['device_name']}".replace(
                        " ", "_"
                    )
                    .replace("/", "_")
                    .replace(":", "_")
                )
                with open(f"yml_configs/{filename}.yaml", "w") as text_file:
                    text_file.write(yml_conf)

def generateConfigs(env, device):
    template = env.get_template(device["template"])
    return template.render(sensor=device)

def clearDir():
    pathPatter = join(getcwd(), "yml_configs/*")
    files = glob(pathPatter)
    for f in files:
        remove(f)

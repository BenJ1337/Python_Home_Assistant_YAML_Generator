#!/usr/bin/env python3

import logging
import argparse

from .sensor import yaml_generator

logger = logging.getLogger(__name__)

def run():
    yaml_generator.generateYAML()

if __name__ == "__main__":
    run()

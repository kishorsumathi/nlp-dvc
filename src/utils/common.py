import yaml
import os
import pickle
import json
import logging


def read_yaml(path_to_yaml:str):
    with open(path_to_yaml) as yaml_file:
        content= yaml.safe_load(yaml_file)
    
    return content
def create_directory(dirs: list):
    for dir_path in dirs:
          os.makedirs(dir_path,exist_ok=True)
          logging.info(f"directory is created at {dir_path}")
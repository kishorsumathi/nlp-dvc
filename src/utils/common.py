import yaml
import os
import pickle
import pandas as pd
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

def get_df(path_to_data: str, sep: str="\t") -> pd.DataFrame:
    df = pd.read_csv(
        path_to_data,
        encoding="utf-8",
        header=None,
        delimiter=sep,
        names=["id", "label", "text"],
    )
    logging.info(f"The input data frame {path_to_data} size is {df.shape}\n")
    return df

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")

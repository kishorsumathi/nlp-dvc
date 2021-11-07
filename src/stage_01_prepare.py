import argparse
import os
from posixpath import split
import random
from tqdm import tqdm
from src.utils.common import read_yaml, create_directory, process
import logging

STAGE="one"


logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

def main(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)

    source_data_dir=config["source_data"]["data_dir"]
    source_data_file=config["source_data"]["data_file"]
    input_data=os.path.join(source_data_dir,source_data_file)
    artifacts= config["artifacts"]
    preapare_dir= artifacts["PREPARE_DATA"]
    create_directory([os.path.join(artifacts["ARTIFACTS_DIR"],artifacts["PREPARE_DATA"])])

    train_data_path=os.path.join(artifacts["ARTIFACTS_DIR"],artifacts["PREPARE_DATA"],artifacts["TRAIN_DATA"])
    test_data_path=os.path.join(artifacts["ARTIFACTS_DIR"],artifacts["PREPARE_DATA"],artifacts["TEST_DATA"])
    split=params["prepare"]["split"]
    seed=params["prepare"]["seed"]

    with open(input_data,encoding="utf8") as fd_in:
        with open(train_data_path,"w",encoding="utf8") as fd_out_train:
            with open(test_data_path,"w",encoding="utf8") as fd_out_test:
                process(fd_in,fd_out_train,fd_out_test,"<python>",split)
          

    random.seed(seed)
   
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config,params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed! all the data are saved in local <<<<<n")
    except Exception as e:
        logging.exception(e)
        raise e
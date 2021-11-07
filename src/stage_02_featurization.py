import argparse
import os
import shutil
from tqdm import tqdm
from src.utils.common import read_yaml, create_directory
from src.utils.data_mng import process
import logging

STAGE="two"
logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

def main(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)


    artifacts= config["artifacts"]
    train_data_path=os.path.join(artifacts["ARTIFACTS_DIR"],artifacts["PREPARE_DATA"],artifacts["TRAIN_DATA"])
    test_data_path=os.path.join(artifacts["ARTIFACTS_DIR"],artifacts["PREPARE_DATA"],artifacts["TEST_DATA"])
    featurized_data_dir_path = os.path.join(artifacts["ARTIFACTS_DIR"], artifacts["FEATURIZED_DATA"])
    create_directory([featurized_data_dir_path])

    featurized_train_data_path = os.path.join(featurized_data_dir_path, artifacts["FEATURIZED_OUT_TRAIN"])
    featurized_test_data_path = os.path.join(featurized_data_dir_path, artifacts["FEATURIZED_OUT_TEST"])
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
import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

from src.exception.exception import CustomException
from src.logger.logging import logging

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "raw_data.csv")
    train_data_path:str = os.path.join("artifacts", "train_data.csv")
    test_data_path:str = os.path.join("artifacts", "test_data.csv")


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion has been started")

        try:
            data = pd.read_csv("https://raw.githubusercontent.com/Urvil-Dhanani/pricepredictor/main/gemstone.csv")
            logging.info("Reading a csv file ...")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data has been saved in Artifact directory.")

            train_data, test_data = train_test_split(data, test_size=0.20)
            logging.info("Train Test splitting done")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Train & Test data are saved in Artifact directory")
            logging.info("DATA INGESTION DONE !!!")

            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e, sys)
        

    

# testing
# ing = DataIngestion()
# ing.initiate_data_ingestion()
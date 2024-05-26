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
            print(data.head(2))
            
        except Exception as e:
            raise CustomException(e, sys)


ing = DataIngestion()
ing.initiate_data_ingestion()
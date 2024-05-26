import os
import sys 
import pandas as pd

from src.logger.logging import logging
from src.exception.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# Data Ingestion
obj = DataIngestion
train_path, test_path = obj.initiate_data_ingestion()

# Data Transformation
transform = DataTransformation()
train_arr, test_arr = transform.initiate_data_transform()

# Model Training
model_trainer = ModelTrainer()
model_trainer.initiate_model_training(train_arr, test_arr)
import os
import sys 
import pandas as pd
import time

from src.logger.logging import logging
from src.exception.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

# # Data Ingestion
# obj = DataIngestion()
# train_path, test_path = obj.initiate_data_ingestion()


# # Data Transformation
# transform = DataTransformation()
# train_arr, test_arr = transform.initiate_data_transform(train_path, test_path)

# # Model Training
# model_trainer = ModelTrainer()
# model_trainer.initiate_model_training(train_arr, test_arr)

# # Model Evaluation
# model_eval = ModelEvaluation()
# model_eval.initiate_evaluation(test_arr)

#  above was for the local testing 
# now we define a class so that we can use this trianing pipeline for 
# Pipeline versioning & tracking 
# for airflow task assign 

class TrainingPipeline:

    def start_data_ingestion(self):
        try:
            obj = DataIngestion()
            train_path, test_path = obj.initiate_data_ingestion()
            return train_path, test_path
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_data_transformation(self, train_path, test_path):
        try:
            transform = DataTransformation()
            train_arr, test_arr = transform.initiate_data_transform(train_path, test_path)
            return train_arr, test_arr
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_model_training(self, train_arr, test_arr):
        try:                
            trainer = ModelTrainer()
            trainer.initiate_model_training(train_arr, test_arr)
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_training(self):
        try:
            train_path, test_path = self.start_data_ingestion()
            train_arr, test_arr = self.start_data_transformation(train_path, test_path)
            self.start_model_training(train_arr, test_arr)
        except Exception as e:
            raise CustomException(e, sys)



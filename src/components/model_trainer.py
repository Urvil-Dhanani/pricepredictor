import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from pathlib import Path

from sklearn.linear_model import ElasticNet, LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from src.exception.exception import CustomException
from src.logger.logging import logging
from src.utils.utils import save_object, evaluate_model
from src.components.data_transformation import DataTransformation

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:

    def __init__(self):
        self.trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_arr, test_arr):
        try:

            x_train, y_train, x_test, y_test = train_arr[:, :-1], train_arr[:, -1], test_arr[:, :-1], test_arr[:, -1]

            models = {
                "LinearRegression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "ElasticNet": ElasticNet(),
                "RF_Regressor": RandomForestRegressor(),
                "XGBoost": XGBRegressor()
            }

            model_report:dict = evaluate_model(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test, models=models)

            print(model_report)
            logging.info(f"Model Report --> {model_report}")

            # Getting best score
            model_best_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(model_best_score)]
            best_model = model_report[best_model_name]

            print(f"Best Model: {best_model_name} \nR2_score: {model_best_score}")
            print(60*"#")
            logging.info(f"Best Model is: {best_model_name}")

            # model saving
            save_object(self.trainer_config.trained_model_path, best_model)


        except Exception as e:
            logging.info("Exception clicked during Model training")
            raise CustomException(e, sys)

# testing 
obj1 = DataTransformation()
train_arr, test_arr = obj1.initiate_data_transform("artifacts/train_data.csv", "artifacts/test_data.csv")

obj = ModelTrainer()
obj.initiate_model_training(train_arr, test_arr)
            





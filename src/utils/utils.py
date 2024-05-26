import os
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

from src.exception.exception import CustomException
from src.logger.logging import logging


def save_object(file_path, object):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(object, file_obj)
            logging.info(f"Object has been saved in {file_path}")

    except Exception as e:
        logging.info("Exception clicked during saving the object")
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    
    except Exception as e:
        logging.info("Exception clicked during loading the object")
        raise CustomException(e, sys)
    
def evaluate_model(x_train, x_test, y_train, y_test, models:dict):

    try:
        report={}
        for i in range(len(models)):

            model = list(models.values())[i]
            model.fit(x_train, y_train)
            logging.info(f"Model: {model} has been trained")

            y_pred = model.predict(x_test)
            model_score = r2_score(y_test, y_pred)

            report[list(models.keys())[i]] = model_score

        return report
    
    except Exception as e:
        logging.info("Exception clicked during model training")
        raise CustomException(e, sys)





    

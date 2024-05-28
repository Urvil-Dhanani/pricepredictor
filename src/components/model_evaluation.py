import pandas as pd
import os
import sys
from urllib.parse import urlparse
import numpy as np
import mlflow
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.logger.logging import logging
from src.exception.exception import CustomException
from src.utils.utils import load_object


class ModelEvaluation:
    def __init__(self):
        print("Evaluation Starts")

    def evaluation_metrics(self, y_true, y_pred):
        MAE = mean_absolute_error(y_true, y_pred)
        MSE = mean_squared_error(y_true, y_pred)
        R2 = r2_score(y_true, y_pred)
        return MAE, MSE, R2
    
    def initiate_evaluation(self, test_df):

        try:

            x_test, y_test = test_df[:,:-1], test_df[:,-1]
            print(type(x_test))
            model_path = os.path.join("artifacts", "model.pkl")
            model = load_object(model_path)

            # # model Registry
            # mlflow.set_registry_uri()

            tracking_url_store_type=urlparse(mlflow.get_tracking_uri()).scheme
            print(tracking_url_store_type)

            with mlflow.start_run():
                
                y_pred = model.predict(x_test)
                MAE, MSE, R2 = self.evaluation_metrics(y_test, y_pred)

                mlflow.log_metric("MAE", MAE)
                mlflow.log_metric("MSE", MSE)
                mlflow.log_metric("R2", R2)

                if tracking_url_store_type != "file":
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model, "model")

        except Exception as e:
            raise CustomException(e, sys)

# testing

# obj = ModelEvaluation()
# test_df = pd.read_csv(os.path.join("artifacts", "test_data.csv"))
# test_df.drop(columns=["id"], axis=1, inplace=True)
# print(test_df.head(3))
# my_df = np.array(test_df)


# # x_test, y_test = my_df[:, :-1], my_df[:, -1]
# # print(x_test.head(3))
# # print(y_test.head(3))
# obj.initiate_evaluation(my_df)
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from pathlib import Path

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.exception.exception import CustomException
from src.logger.logging import logging
from src.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:

    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def transorm_data(self):
        try:
            logging.info("Transformation starting ...")

            # Segregate categorical & numerical columns
            cat_cols = ['cut', 'color','clarity']
            num_cols = ['carat', 'depth','table', 'x', 'y', 'z']

            # Ranking for ordinal columns (Ascending)
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info("Initiating pipeline")
        
            # Numerical pipeline
            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            # Categorical pipeline
            cat_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder", OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories]))
                ]
            )

            # Preparing the preprocessor
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipe", num_pipeline, num_cols),
                    ("cat_pipe", cat_pipeline, cat_cols)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        

    
    def initiate_data_transform(self, train_path, test_path):
        try:

            preprocessor_obj = self.transorm_data()
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            lable_name ="price"
            remove_cols = ["id","price"]

            # splitting features and lable - train data
            feature_train_df = train_df.drop(columns=remove_cols, axis=1)
            lable_train_df = train_df[lable_name]

            # splitting features and lable - test data
            feature_test_df = test_df.drop(columns=remove_cols, axis=1)
            lable_test_df = test_df[lable_name]

            # processing on train & test features
            feature_train_arr = preprocessor_obj.fit_transform(feature_train_df)
            feature_test_arr = preprocessor_obj.transform(feature_test_df)

            # concatinating features and lable to make a full dataset
            train_dataset = np.c_[feature_train_arr, np.array(lable_train_df)]
            test_dataset = np.c_[feature_test_arr, np.array(lable_test_df)]

            save_object(self.transformation_config.preprocessor_obj_path, preprocessor_obj)
            logging.info("Preprocessor Object saved !!")

            return (train_dataset, test_dataset)
        
        except Exception as e:
            raise CustomException(e, sys)


# testing
# obj = DataTransformation()
# obj.initiate_data_transform("artifacts/train_data.csv", "artifacts/test_data.csv")



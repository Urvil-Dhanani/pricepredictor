import os
import sys
import pandas as pd

from src.exception.exception import CustomException
from src.logger.logging import logging
from src.utils.utils import load_object

class PredictPipeline:

    def __init__(self):
        print("Prediction starts ...")

    def predict(self, dataframe):

        try:
            # Getting path for preprocessor & model
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl" )
            model_path = os.path.join("artifacts", "model.pkl")

            # Loading preprocessor & model
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            # perform processing & prediction
            processed_data = preprocessor.transform(dataframe)
            print("Features are processed")
            predicted_data = model.predict(processed_data)

            return predicted_data
    
        except Exception as e:  
            logging.info("Exception occured at Prediction")
            raise CustomException(e, sys)
        
class CustomData:
    def __init__(self, carat:float, cut:str, color:str, clarity:str, depth:float, table:float, x:float, y:float, z:float):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z


    def data_to_dataframe(self):
        try:
            input_data_dict = {
                "carat":[self.carat],
                "cut":[self.cut],
                "color":[self.color],
                "clarity":[self.clarity],
                "depth":[self.depth],
                "table":[self.table],
                "x":[self.x],
                "y":[self.y],
                "z":[self.z]
            }

            df = pd.DataFrame(input_data_dict)
            logging.info("Dataframe generated from user input")
            return  df
        except Exception as e:
            logging.info("Exception clicked in prediction pipeline")
            raise CustomException(e, sys)

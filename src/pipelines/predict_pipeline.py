import sys
import os
import pandas as pd
import numpy as np
from src.utils import CustomException
from src.utils import load_object
from src.logger import logging




class PredictPipeline:
    def __init__(self):
        # No input is required to the class, just input is needed for the function predict
        # we could have made a simple function predict instead of making class
        pass
    def predict(self,features):
        try:
            model_path = os.path.join('artifacts', 'trained_model.pkl')
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled)

            return prediction
        except Exception as e:
            raise CustomException(e, sys)
        
    
        




# Specifying or fixing the data types of the columns for getting inputs from web application
class CustomData:
    # These all inputs will be taken from the web application
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    
    # this function will just return input data from web app as a dataframe
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

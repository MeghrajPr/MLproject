import os
import sys
from dataclasses import dataclass

#from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
#from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'trained_model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def Initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting the training and test data")

            X_train, y_train, X_test, y_test = (
                train_array[:,:-1], 
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models ={
                'Linear Regression': LinearRegression(),
                'Decision Tree': DecisionTreeRegressor(),
                'Random Forest': RandomForestRegressor(),
                'AdaBoost': AdaBoostRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'KNN': KNeighborsRegressor()
            }
            logging.info("Starrting the model training process")

            model_report:dict =evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test,y_test= y_test, models=models)

            # finding the best model score

            best_model_score = max(sorted(model_report.values()))

            # getting the best model name

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]


            if best_model_score<0.6:
                raise CustomException("Model score is less than 0.6",sys)
            
            best_model = models[best_model_name]
            
            logging.info(f"Best model is {best_model_name} with score {best_model_score}")


            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model

            )

            logging.info("Model training, evaluation and saving is completed")

            return best_model_score


            
        except Exception as e:
            raise CustomException(e,sys)

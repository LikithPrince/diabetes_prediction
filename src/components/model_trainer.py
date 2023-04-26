import os
import sys
from dataclasses import dataclass

# Modelling
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostClassifier
from xgboost import XGBClassifier

from src.exception import CustomException
from src.logger import logging
from src.utils import *
# from hyperparameter_config import params


@dataclass
class ModelTrainerConfig:
   trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
   def __init__(self):
      self.model_trainer_config = ModelTrainerConfig()

   def initiate_model_trainer(self, train_array, test_array):
      try:
         logging.info("Split training and testing input data")
         x_train, y_train, x_test, y_test = (
            train_array[:,:-1],
            train_array[:,-1],
            test_array[:,:-1],
            test_array[:,-1]
         )
         models = {
            "Decision Tree Classifier": DecisionTreeClassifier(),
            "Random Forest Classifier": RandomForestClassifier(),
            "Linear Classifier": LinearRegression(),
            "XGBoost Classifier": XGBClassifier(),
            "CatBoost Classifier": CatBoostClassifier(verbose = False),
            "AdaBoost Classifier": AdaBoostClassifier(),
            "KNeighbors Classifier": KNeighborsClassifier(),
            "SVM Classifier": SVC()
         }

         model_report : dict = evaluate_models(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test, models = models)
         best_model_score = max(sorted(model_report.values()))
         logging.info("Best model score: {}".format(best_model_score))
         best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
         ]
         best_model = models[best_model_name]
         logging.info("Best model: {}".format(best_model))
         print("Best model: {}".format(best_model))

         if best_model_score<0.6:
            raise CustomException("No best model found.")
         logging.info("Best model found on both training and testing datasets")

         save_object(
            file_path = self.model_trainer_config.trained_model_file_path,
            obj = best_model
         )
         predicted = best_model.predict(x_test)
         r2_scor = r2_score(y_test,predicted)
         return r2_scor
      

      except Exception as e:
         raise CustomException(e, sys)
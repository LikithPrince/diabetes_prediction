import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
   train_data_path = os.path.join("artifacts","train.csv")
   test_data_path = os.path.join("artifacts","test.csv")
   raw_data_path = os.path.join("artifacts","raw_data.csv")

class DataIngestion:
   def __init__(self):
      self.ingestion_config = DataIngestionConfig()

   def initiate_data_ingestion(self):
      logging.info("Starting data ingestion")
      logging.info("Training data path: {}".format(self.ingestion_config.train_data_path))
      logging.info("Test data path: {}".format(self.ingestion_config.test_data_path))
      logging.info("Raw data path: {}".format(self.ingestion_config.raw_data_path))
      try:
         df = pd.read_csv('notebook/data/diabetes_prediction_dataset.csv')
         os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
         df.to_csv(self.ingestion_config.raw_data_path, index = False)

         train_df, test_df = train_test_split(df, test_size=0.2, random_state= 70)
         train_df.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
         test_df.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

         return ( self.ingestion_config.train_data_path,
                  self.ingestion_config.test_data_path)
      except Exception as e:
         raise CustomException(e, sys)
      

if __name__ == "__main__":
   data_ingestion = DataIngestion()
   train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

   data_transformation = DataTransformation()
   train_array, test_array = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

   modeltrainer = ModelTrainer()
   r2_score = modeltrainer.initiate_model_trainer(train_array , test_array)
   print("R-2 Score : ", r2_score)


import os
import sys
from src.exceptions import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

# DataIngestionConfig class with default file paths for train, test, and raw data
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts', "train.csv") # Path to save training data
    test_data_path:str=os.path.join('artifacts', "test.csv")   # Path to save testing data
    raw_data_path:str=os.path.join('artifacts', "raw.csv")     # Path to save raw data
    
# Data ingestion class to handle data loading and preparation    
class DataIngestion:
    # Initialize DataIngestionConfig with paths for data storage
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    # Method to initiate data ingestion process
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df=pd.read_csv('C:/mlproject/notebook/data/StudentsPerformance.csv')
            logging.info("Read the dataset as dataframe")
            
            # Ensure the directory for data storage exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Save the raw data for future reference or reuse
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df, test_size=0.3, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")
            
            # Return paths to the train and test data files
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys) 
    
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data,test_data)
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
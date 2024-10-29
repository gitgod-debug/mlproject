import os
import sys
from src.exceptions import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def run_pipeline(self):
        try:
            # Step 1: Data Ingestion
            logging.info("Starting data ingestion...")
            train_data_path, test_data_path = self.data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed. Train data at {train_data_path}, Test data at {test_data_path}")

            # Step 2: Data Transformation
            logging.info("Starting data transformation...")
            # Call the method to initiate data transformation
            transformation_result = self.data_transformation.initiate_data_transformation(train_data_path, test_data_path)
            # Unpack the results from the transformation
            train_array, test_array, preprocessor_path = transformation_result
            logging.info("Data transformation completed.")

            # Step 3: Model Training
            logging.info("Starting model training...")
            model_training_result = self.model_trainer.initiate_model_trainer(train_array, test_array)
            # Extract model path and R² score from the result
            trained_model_path = model_training_result["model_path"]
            r2_score = model_training_result["r2_score"]
            logging.info(f"Model training completed. Model saved at {trained_model_path}")
        
        except Exception as e:
            logging.error(f"Error occurred in the training pipeline: {e}")
            raise CustomException(e, sys)

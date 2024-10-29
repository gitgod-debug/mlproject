import os
import sys

import dill          # A pickle extension for serializing objects
import pickle        # # A standard module for serializing and saving objects
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exceptions import CustomException

# Function to save a Python object to a file
def save_object(file_path, obj):
    try:
        # Get the directory path from the file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it does not exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in write-binary mode and serialize the object to the file
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
# Function to evaluate and tune multiple models using GridSearchCV
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        # Dictionary to store the test score of each model
        report = {}

        # Iterate over each model and its corresponding parameters
        for i in range(len(list(models))):
            model = list(models.values())[i]  # Access the model instance
            para=param[list(models.keys())[i]]  # Access the parameter grid for this model

            # Perform grid search cross-validation with the specified parameters
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            # Update model with the best parameters from grid search
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)  # Train the model with best parameters

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            # Save the test score in the report dictionary with the model name as the key
            report[list(models.keys())[i]] = test_model_score

        return report  # Return the report dictionary with test scores for each model

    except Exception as e:
        raise CustomException(e, sys)
    
# Function to load a serialized Python object from a file
def load_object(file_path):
    try:
        # Open the file in read-binary mode and load the object
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
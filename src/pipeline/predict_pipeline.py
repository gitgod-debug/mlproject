import os
import sys
import pandas as pd
from src.exceptions import CustomException
from src.utils import load_object

# PredictPipeline class to handle prediction workflow
class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        """
        Predicts outcomes based on input features.
        
        Parameters:
            features (pd.DataFrame): A DataFrame containing input features for prediction.
        
        Returns:
            preds (np.array): Array of predicted values.
        
        Raises:
            CustomException: If any error occurs during the prediction process.
        """
        try:
            # Define the file paths for the model and preprocessor artifacts
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            
            print("Before Loading")
            
            # Load the model and preprocessor objects from the specified paths
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)           
            
            print("After Loading")
            
            # Transform input features using the preprocessor
            data_scaled=preprocessor.transform(features)
            
            # Generate predictions using the loaded model
            preds=model.predict(data_scaled)
            
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


# CustomData class to format and store input data as a DataFrame
class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
        """
        Initializes the CustomData object with given parameters.

        Parameters:
            gender (str): Gender of the student.
            race_ethnicity (str): Race/ethnicity group of the student.
            parental_level_of_education (str): Parent's education level.
            lunch (str): Type of lunch provided.
            test_preparation_course (str): Whether the student took a test prep course.
            reading_score (int): Reading score of the student.
            writing_score (int): Writing score of the student.
        """
        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """
            Converts the initialized data into a DataFrame.

            Returns:
                pd.DataFrame: A DataFrame containing the custom data inputs.
        
            Raises:
                CustomException: If any error occurs during DataFrame creation.
        """
        try:
            # Create a dictionary with each attribute as a list (to fit DataFrame format)
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score],
            }
            
            # Return the dictionary as a DataFrame
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
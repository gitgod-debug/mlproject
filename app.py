import os
import logging
from flask import Flask,request,render_template

from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from src.pipeline.train_pipeline import TrainPipeline

app=Flask(__name__)

## Route for a home page
'''
To access prediction route, use the following URL: http://127.0.0.1:5000/predictdata
'''
@app.route('/')  # Defines the route for the root URL
def index():
    return render_template('index.html')  # Renders the main index page (HTML template)

# Route for handling prediction data input
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    # If the request method is GET, show the form to enter data
    if request.method=='GET':
        return render_template('home.html')
    else:
        # If the method is POST, process the submitted form data
        # Create an instance of CustomData with form data
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),  # Convert input to float
            writing_score=float(request.form.get('reading_score'))   # Convert input to float

        )
        
        # Convert the data to a DataFrame format required for prediction
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        # Initialize prediction pipeline
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        
        # Run prediction on the DataFrame
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        
        # Render the result on the home page
        return render_template('home.html',results=results[0])
    
# Route for initiating the model training 
'''
To access train route, use the following URL: http://127.0.0.1:5000/predictdata
'''
@app.route('/train', methods=['GET'])
def train_model():
    try:
        # Initialize and run the training pipeline
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        
        return render_template('home.html', results="Model training completed successfully.")
    except Exception as e:
        logging.error(f"Training error: {e}", exc_info=True)  # Log the error with traceback
        return render_template('home.html', results=f"Error occurred during training: {str(e)}")
    
# Main driver function for running the Flask app
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host="0.0.0.0", debug=True)  # Run the app on the local server (listening on all public IPs) 
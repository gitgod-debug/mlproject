# MLProject

The mlproject is a robust, end-to-end machine learning application designed to guide users through every stage of the ML workflow, from data handling to deployment. This project demonstrates essential machine learning tasks such as data preprocessing, feature engineering, model training, and evaluation, all structured within a modular pipeline. It uses tools like MLflow for experiment tracking, enabling users to record and compare model performance effectively.

This project is configured to be deployed on Render, supporting flexible and cloud-based deployment options, making it adaptable for various environments. It can be run locally as well, allowing for quick adjustments in parameters and settings to fine-tune model behavior. While deployed services on free platforms like Render may go offline due to inactivity limitations, the project remains accessible for continued development and experimentation on local machines.

---

## Project Overview

The **MLProject** is designed to guide users through each stage of the machine learning workflow, with a primary focus on building a modular pipeline that is easy to adapt, debug, and scale. Key stages include:

- **Data Handling & Preprocessing:** Clean and prepare data, perform feature engineering, and handle missing values.
- **Experiment Tracking:** Use MLflow to record and compare model metrics.
- **Model Training & Evaluation:** Train machine learning models, evaluate performance, and fine-tune model parameters.
- **Deployment on Render:** Deploy the application to Render for cloud-based access (though note that free-tier deployments go offline after 15 minutes of inactivity).

---

## Project Structure

- `app.py`: The main application script containing Flask routes for model prediction and training.
- `notebook/`: Contains data and experiments
- `src/`: Contains all pipeline code, including data processing, model training, and prediction logic.
- `templates/`: HTML templates for the web interface.

---

## Installation

To set up and run this project on your local system, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/gitgod-debug/mlproject.git

cd mlproject
```


---

## Key Technologies

<p align="left">
  <img src="https://github.com/gitgod-debug/mlproject/blob/main/Images/Flask.webp" width="200" height="200"/>
  <img src="https://github.com/gitgod-debug/mlproject/blob/main/Images/Numpy.webp" width="200" height="200"/>
  <img src="https://github.com/gitgod-debug/mlproject/blob/main/Images/pandas.webp" width="200" height="200"/>
  <img src="https://github.com/gitgod-debug/mlproject/blob/main/Images/Python.webp" width="200" height="200"/>
  <img src="https://github.com/gitgod-debug/mlproject/blob/main/Images/sklearn.webp" width="200" height="200"/>
  <img src="https://github.com/gitgod-debug/mlproject/blob/main/Images/HTML_CSS.webp" width="200" height="200"/>
</p>

---

## Install Dependencies

Make sure you have Python installed. Then install the required packages.

```cmd
pip install -r requirements.txt

```


---

## Run the Application:

```cmd
python app.py

```

---

## Navigate to the App

Open your browser and go to:

Home: 
```
http://127.0.0.1:5000/
```

Predict Data:
```
http://127.0.0.1:5000/predictdata
```

Train Model:
```
http://127.0.0.1:5000/train
```

---

## Usage

The project can be run locally or deployed to cloud platforms like Render. Configuration and parameter files allow for easy adjustments to model settings, ensuring flexibility for different use cases.

> **Note**: This project was deployed on Render; however, due to inactivity limits on the free tier, the deployed services may go offline after 15 minutes.

---

## Credits

This project is inspired by the MLProject tutorial series by **Krish Naik**, who provided detailed insights into structuring and deploying end-to-end machine learning pipelines.

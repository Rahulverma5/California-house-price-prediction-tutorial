# California Housing Price Prediction

## Overview

This project implements a machine learning model to predict housing prices in California based on various features like median income, house age, average rooms, and geographic location. The model is deployed as both a Flask API and a Streamlit web application, providing multiple ways to interact with the prediction service.

## Dataset

The project uses the California Housing dataset from scikit-learn, which contains information collected from the 1990 California census. It includes features such as:

- Median income in the block group
- House age in the block group
- Average number of rooms
- Average number of bedrooms
- Population in the block group
- Average occupancy
- Latitude and Longitude


## Project Structure

```
├── california_housing_prediction.ipynb   # Jupyter notebook with data analysis and model development
├── rf_model.pkl                          # Serialized Random Forest model
├── app.py                                # Flask API implementation
├── web_app.py                            # Streamlit web application
└── requirements.txt                      # Dependencies required for the project
```


## Features

- **Data Exploration**: Comprehensive analysis of the California housing dataset
- **Feature Engineering**: Creation of new features to improve model performance
- **Model Training**: Implementation of Random Forest Regressor with hyperparameter tuning
- **API Endpoint**: RESTful API for housing price prediction
- **Interactive Web App**: User-friendly interface for making predictions
- **Deployment**: Model deployed on Hugging Face Spaces using Streamlit


## Installation \& Setup

### Prerequisites

- Python 3.7+
- pip


### Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/Rahulverma5/California-house-price-prediction-tutorial.git
cd California-house-price-prediction-tutorial
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the Flask API
```bash
python app.py
```

4. Run the Streamlit web app
```bash
streamlit run web_app.py
```


## Usage

### Flask API

The API exposes a `/predict` endpoint that accepts POST requests with JSON data containing housing features:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.023810,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23
  }'
```

Response:

```json
{
  "predicted_price": 4.526
}
```


### Streamlit Web App

The Streamlit app provides an interactive interface where users can:

- Adjust feature values using sliders
- Visualize the impact of different features on the predicted price
- Get instant predictions based on the selected values


## Methodology

1. **Data Preprocessing**: Handling missing values and scaling features
2. **Feature Engineering**: Creating 'BedroomRatio' and 'RoomsPerPerson' features
3. **Model Selection**: Comparing multiple regression models including Linear Regression, Ridge, Lasso, Random Forest, and Gradient Boosting
4. **Hyperparameter Tuning**: Using RandomizedSearchCV and GridSearchCV to optimize model parameters
5. **Model Evaluation**: Assessing performance using RMSE, MAE, and R² scores

## Results

The Random Forest model achieved the best performance with:

- R² score: 0.82 on the test set
- RMSE: 0.49 (in scaled units of median house value)
- MAE: 0.31 (in scaled units of median house value)


## Deployment

The model is deployed in two ways:

1. As a Flask API that can be integrated into other applications
2. As a Streamlit web app hosted on Hugging Face Spaces for interactive use

## Future Improvements

- Integrate additional external datasets (e.g., crime rates, school ratings)
- Implement more advanced models like XGBoost or Neural Networks
- Add time-series analysis to track price changes over time
- Create a more comprehensive dashboard with additional visualizations
- Implement feature importance explanations using SHAP or LIME


## License

This project is open source and available under the MIT License.

## Author

Rahul Verma

## Acknowledgments

- scikit-learn for providing the California Housing dataset
- Streamlit for the easy-to-use web app framework
- Flask for the lightweight API framework


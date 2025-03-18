import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load saved model and scaler
with open("rf_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
scaler = model_data["scaler"]
original_features = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup",
    "Latitude", "Longitude"
]

# Function to make predictions
def predict_price(features):
    # Convert input to DataFrame
    input_df = pd.DataFrame([features], columns=original_features)

    # Apply feature engineering
    input_df["BedroomRatio"] = input_df["AveBedrms"] / input_df["AveRooms"]
    input_df["RoomsPerPerson"] = input_df["AveRooms"] / input_df["AveOccup"]

    # Scale features
    input_scaled = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(input_scaled)

    return round(prediction[0], 2)

# Streamlit App UI
st.set_page_config(page_title="California House Price Predictor", page_icon="🏠", layout="wide")

st.title("🏡 California House Price Predictor")
st.write("Enter the values of house attributes to get an estimated price!")

# Sidebar with user inputs
st.sidebar.header("Input Features")

medinc = st.sidebar.slider("Median Income (in $10,000)", 0.5, 15.0, 3.5)
house_age = st.sidebar.slider("House Age (years)", 1, 52, 20)
avg_rooms = st.sidebar.slider("Average Rooms per Household", 1.0, 10.0, 5.2)
avg_bedrooms = st.sidebar.slider("Average Bedrooms per Household", 0.5, 5.0, 1.1)
population = st.sidebar.number_input("Population in Block", min_value=100, max_value=40000, value=1500)
avg_occupancy = st.sidebar.slider("Average Occupancy", 1.0, 10.0, 3.0)
latitude = st.sidebar.slider("Latitude", 32.5, 42.0, 34.0)
longitude = st.sidebar.slider("Longitude", -125.0, -114.0, -118.0)

# Predict Button
if st.sidebar.button("🔍 Predict House Price"):
    input_values = [medinc, house_age, avg_rooms, avg_bedrooms, population, avg_occupancy, latitude, longitude]
    price = predict_price(input_values)

    # Display result beautifully
    st.success(f"💰 Estimated House Price: **${price * 100000:,.2f}**")

    # Add an inspiring message
    st.write("✨ Find your dream home at the right price! ✨")

# Footer
st.markdown("---")
st.markdown("🔥 *Built with ❤️ using Streamlit & Machine Learning*")

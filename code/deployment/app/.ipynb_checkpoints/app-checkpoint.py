import streamlit as st
import requests

st.title("California Housing Price Prediction")

MedInc = st.number_input("Median Income")
HouseAge = st.number_input("House Age")
AveRooms = st.number_input("Average Rooms")
AveBedrms = st.number_input("Average Bedrooms")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Make Prediction"):
    features = [MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]
    try:
        response = requests.post("http://api:8000/predict/", json={"features": features})
        response_data = response.json()
        st.write("API Response:", response_data)

        if 'prediction' in response_data:
            st.success(f"Predicted Price: ${response_data['prediction']:.2f}")
        else:
            st.error("The 'prediction' key is missing in the response.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

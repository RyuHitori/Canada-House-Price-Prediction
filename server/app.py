import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/canada_home_prices_model.joblib")

st.title("🇨🇦 Canada House Price Prediction")

city = st.text_input("City")
province = st.selectbox("Province", ["ON", "BC", "AB", "QC"])
bedrooms = st.number_input("Bedrooms", 0, 10, 3)
bathrooms = st.number_input("Bathrooms", 0, 10, 2)
acreage = st.number_input("Acreage", 0.0, 10.0, 0.5)
sqft = st.number_input("Square Footage", 100, 10000, 1500)

if st.button("Predict Price"):
    data = pd.DataFrame([{
        "City": city,
        "Province": province,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Acreage": acreage,
        "Square Footage": sqft
    }])

    price = model.predict(data)[0]
    st.success(f"Estimated Price: ${price:,.0f}")

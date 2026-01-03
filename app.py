import streamlit as st
import pandas as pd
import joblib
import json
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_PATH = os.path.join(MODEL_DIR, "canada_home_prices_model.joblib")
CATEGORIES_PATH = os.path.join(MODEL_DIR, "categories.json")
DATA_COLUMNS_PATH = os.path.join(MODEL_DIR, "columns.json")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

try:
    with open(CATEGORIES_PATH, "r") as f:
        categories = json.load(f)
except Exception as e:
    st.error(f"Error loading categories.json: {e}")
    st.stop()

try:
    with open(DATA_COLUMNS_PATH, "r") as f:
        data_columns = json.load(f)["data_columns"]
except Exception as e:
    st.error(f"Error loading data_columns.json: {e}")
    st.stop()

st.title("Canada House Price Prediction")

city = st.selectbox("City", categories["city"])
province = st.selectbox("Province", categories["province"])
bedrooms = st.number_input("Bedrooms", 0, 10, 3)
bathrooms = st.number_input("Bathrooms", 0, 10, 2)
acreage = st.number_input("Acreage", 0.0, 10.0, 0.5)
square_footage = st.number_input("Square Footage", 100, 10000, 1500)
property_type = st.selectbox("Property Type", categories["property type"])
garage = st.selectbox("Garage", categories["garage"])
parking = st.selectbox("Parking", categories["parking"])
fireplace = st.selectbox("Fireplace", categories["fireplace"])
heating = st.selectbox("Heating", categories["heating"])
waterfront = st.selectbox("Waterfront", categories["waterfront"])
sewer = st.selectbox("Sewer", categories["sewer"])
pool = st.selectbox("Pool", categories["pool"])
garden = st.selectbox("Garden", categories["garden"])
balcony = st.selectbox("Balcony", categories["balcony"])


if st.button("Predict Price"):
    input_data = {
        "city": city,
        "province": province,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "acreage": acreage,
        "square_footage": square_footage,
        "property_type": property_type,
        "garage": garage,
        "parking": parking,
        "fireplace": fireplace,
        "heating": heating,
        "waterfront": waterfront,
        "sewer": sewer,
        "pool": pool,
        "garden": garden,
        "balcony": balcony
    }

    df = pd.DataFrame([input_data])

    for col in data_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[data_columns]

    try:
        price = model.predict(df)[0]
        st.success(f"Estimated Price: ${price:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

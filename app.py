import streamlit as st
import pandas as pd
import joblib
import json

# Load model
model = joblib.load("model/canada_home_prices_model.joblib")

with open("model/categories.json", "r") as f:
    categories = json.load(f)

with open("model/data_columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

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
        "property type": property_type,
        "square footage": square_footage,
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

    # 🔑 CRITICAL: align columns
    df = df.reindex(columns=data_columns, fill_value=0)

    price = model.predict(df)[0]
    st.success(f"Estimated Price: ${price:,.0f}")


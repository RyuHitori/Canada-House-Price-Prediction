import pickle
import joblib
import pandas as pd

__model = None
__feature_columns = None


def load_saved_artifacts():
    global __model, __feature_columns
    print("Loading saved model...")

    __model = joblib.load("D:/Canada-House-Price-Prediction/model/house_price_model.joblib")


    __feature_columns = __model.feature_names_in_
    print("Model loaded successfully")

    print("Model loaded successfully")


def get_estimated_price(input_data: dict):
    """
    input_data: dict with keys EXACTLY matching training columns
    """

    df = pd.DataFrame([input_data])

    # Ensure same column order as training
    df = df[__feature_columns]

    prediction = __model.predict(df)[0]
    return round(float(prediction), 2)

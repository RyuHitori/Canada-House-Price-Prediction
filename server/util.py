import joblib
import json
import pandas as pd

__model = None
__feature_columns = None
__categories = None


def load_saved_artifacts():
    global __model, __feature_columns, __categories
    print("Loading saved model...")

    __model = joblib.load(
        "D:/Canada-House-Price-Prediction/model/house_price_model.joblib"
    )

    __feature_columns = list(__model.feature_names_in_)

    with open(
        "D:/Canada-House-Price-Prediction/model/categories.json", "r"
    ) as f:
        __categories = json.load(f)

    print("Model and categories loaded successfully")


def get_categories():
    return __categories


def get_estimated_price(input_data: dict):
    df = pd.DataFrame([input_data])

    # Ensure correct feature order and fill missing safely
    df = df.reindex(columns=__feature_columns, fill_value=0)

    prediction = __model.predict(df)[0]
    return round(float(prediction), 2)

import pandas as pd
import numpy as np
import joblib
from app.model import model

# Load transformation & Column info
scaler = joblib.load("app/preprocessing/scaler2.pkl")
dummy_columns = joblib.load("app/preprocessing/dummy_columns.pkl")
selected_features = joblib.load("app/artifacts/selected_features.pkl")


def make_prediction(input_dict: dict):
    # covert input to single-row DataFrame
    input_df = pd.DataFrame([input_dict])

    # scale numerical columns
    features = ["milage", "gear", "horsepower"]
    input_df[features] = scaler.transform(input_df[features])

    # One_hot encode columns to match training
    input_encoded = pd.get_dummies(input_df)

    # Align with dummy columns from training
    input_encoded = input_encoded.reindex(columns=dummy_columns, fill_value=0)

    # Select final features
    input_final = input_encoded[selected_features]

    # Predict log(price), then Inverse
    prediction_log = model.predict(input_final)
    predicted_price = np.expm1(prediction_log[0])

    return round(predicted_price, 2)

import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "delay_model.pkl")

model = joblib.load(MODEL_PATH)

FEATURE_ORDER = [
    'Delivery_Distance_km',
    'Delivery_Days',
    'Shipment_Temperature_C',
    'Traffic_Level_Encoded',
    'Courier_Type',
    'Warehouse_Hub',
    'State',
    'City',
    'Category',
    'Payment_Method'
]

def predict_delay(static_features, iot_features):
    data = {**static_features, **iot_features}
    df = pd.DataFrame([data])
    df = df[FEATURE_ORDER]
    risk = model.predict_proba(df)[0][1]
    return risk

def get_feature_importance():
    return dict(zip(FEATURE_ORDER, model.feature_importances_))
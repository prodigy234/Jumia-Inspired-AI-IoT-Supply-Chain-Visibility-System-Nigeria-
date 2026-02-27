import os
import joblib
import pandas as pd

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "delay_model.pkl"
)

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

# import joblib
# import pandas as pd

# model = joblib.load("models/delay_model.pkl")

# def predict_delay(static_features, iot_features):
#     data = {**static_features, **iot_features}
#     df = pd.DataFrame([data])
#     risk = model.predict_proba(df)[0][1]
#     return risk
import joblib
import pandas as pd

model = joblib.load("models/delay_model.pkl")

def predict_delay(static_features, iot_features):
    data = {**static_features, **iot_features}
    df = pd.DataFrame([data])
    risk = model.predict_proba(df)[0][1]
    return risk
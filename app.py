import streamlit as st
import pandas as pd
from src.iot_simulator import generate_iot_data
from src.predict import predict_delay

st.set_page_config(
    page_title="AI Supply Chain Visibility",
    layout="wide"
)

st.title("AI-Powered Supply Chain Visibility System")

st.sidebar.header("Shipment Details")

static_features = {
    "Delivery_Distance_km": st.sidebar.slider("Distance (km)", 10, 1000, 250),
    "Delivery_Days": st.sidebar.slider("Expected Days", 1, 14, 5),
    "Shipment_Temperature_C": st.sidebar.slider("Temperature (°C)", 15, 40, 28),
    "Traffic_Level_Encoded": st.sidebar.selectbox("Traffic Level", [0,1,2]),
    "Courier_Type": 1,
    "Warehouse_Hub": 1,
    "State": 1,
    "City": 1,
    "Category": 1,
    "Payment_Method": 1
}

st.subheader("📡 Live IoT Sensor Feed")
iot_data = generate_iot_data()
st.json(iot_data)

risk_score = predict_delay(static_features, {
    "Traffic_Level_Encoded": iot_data['traffic'],
    "Shipment_Temperature_C": iot_data['temperature'],
    "Delivery_Distance_km": iot_data['distance_remaining']
})

st.subheader("AI Delay Prediction")
st.metric("Delay Risk Probability", f"{risk_score*100:.2f}%")

if risk_score > 0.7:
    st.error("HIGH RISK: Immediate action required")
elif risk_score > 0.4:
    st.warning("MEDIUM RISK: Monitor closely")
else:
    st.success("LOW RISK: On track")
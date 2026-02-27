import streamlit as st
import plotly.express as px
from src.iot_simulator import generate_iot_data
from src.predict import predict_delay

st.title("📊 Live Shipment Risk Dashboard")

static_features = {
    "Delivery_Distance_km": st.slider("Distance (km)", 10, 1000, 250),
    "Delivery_Days": st.slider("Expected Days", 1, 14, 5),
    "Shipment_Temperature_C": st.slider("Temperature (°C)", 15, 40, 28),
    "Traffic_Level_Encoded": st.selectbox("Traffic Level", [0,1,2]),
    "Courier_Type": 1,
    "Warehouse_Hub": 1,
    "State": 1,
    "City": 1,
    "Category": 1,
    "Payment_Method": 1
}

iot_data = generate_iot_data()

risk_score = predict_delay(static_features, {
    "Traffic_Level_Encoded": iot_data['traffic'],
    "Shipment_Temperature_C": iot_data['temperature'],
    "Delivery_Distance_km": iot_data['distance_remaining']
})

col1, col2, col3 = st.columns(3)

col1.metric("🚦 Delay Risk", f"{risk_score*100:.2f}%")
col2.metric("🌡 Temperature", iot_data["temperature"])
col3.metric("🚚 Traffic", iot_data["traffic"])

if risk_score > 0.7:
    st.error("HIGH RISK")
elif risk_score > 0.4:
    st.warning("MEDIUM RISK")
else:
    st.success("LOW RISK")
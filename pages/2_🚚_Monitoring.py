import streamlit as st
import pandas as pd
from datetime import datetime
from src.iot_simulator import generate_iot_data
from src.predict import predict_delay

st.title("🚚 Shipment Monitoring Center")

# Initialize session storage
if "shipment_log" not in st.session_state:
    st.session_state.shipment_log = []

st.subheader("📡 Live IoT Sensor Feed")

iot_data = generate_iot_data()
st.json(iot_data)

static_features = {
    "Delivery_Distance_km": iot_data["distance_remaining"],
    "Delivery_Days": 5,
    "Shipment_Temperature_C": iot_data["temperature"],
    "Traffic_Level_Encoded": iot_data["traffic"],
    "Courier_Type": 1,
    "Warehouse_Hub": 1,
    "State": 1,
    "City": 1,
    "Category": 1,
    "Payment_Method": 1
}

risk_score = predict_delay(static_features, {})

status = "LOW"
if risk_score > 0.7:
    status = "HIGH"
elif risk_score > 0.4:
    status = "MEDIUM"

shipment_record = {
    "Timestamp": datetime.now(),
    "Distance_Remaining": iot_data["distance_remaining"],
    "Temperature": iot_data["temperature"],
    "Traffic": iot_data["traffic"],
    "Risk_Score": round(risk_score, 4),
    "Risk_Level": status
}

st.session_state.shipment_log.append(shipment_record)

st.subheader("📊 Shipment Activity Log")
df = pd.DataFrame(st.session_state.shipment_log)
st.dataframe(df, use_container_width=True)

st.metric("Latest Risk Score", f"{risk_score*100:.2f}%")

if status == "HIGH":
    st.error("⚠️ HIGH RISK SHIPMENT DETECTED")
elif status == "MEDIUM":
    st.warning("⚠️ Moderate Risk — Monitor Closely")
else:
    st.success("✅ Shipment Operating Normally")
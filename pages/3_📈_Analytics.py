import streamlit as st
import plotly.express as px
from src.predict import get_feature_importance

st.title("📈 AI Model Analytics")

importance = get_feature_importance()

fig = px.bar(
    x=list(importance.values()),
    y=list(importance.keys()),
    orientation="h",
    title="Feature Importance",
    color=list(importance.values()),
    color_continuous_scale="Oranges"
)

st.plotly_chart(fig, use_container_width=True)
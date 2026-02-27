import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Jumia AI Supply Chain",
    page_icon="📦",
    layout="wide",
)

# ---- CUSTOM CSS (JUMIA STYLE) ----
st.markdown("""
<style>
body {
    background-color: #111111;
}
.stApp {
    background-color: #111111;
    color: white;
}
h1, h2, h3 {
    color: #F68B1E;
}
.stMetric {
    background-color: #1c1c1c;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;'>📦 Jumia AI Supply Chain Intelligence</h1>
<p style='text-align:center;'>Real-Time Delay Risk Monitoring Powered by AI + IoT</p>
""", unsafe_allow_html=True)

st.image("assets/ihenacho_image.jpeg", width=200)

st.success("Navigate using the sidebar to explore features.")
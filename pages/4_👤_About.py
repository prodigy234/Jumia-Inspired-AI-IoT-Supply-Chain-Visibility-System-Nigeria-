import streamlit as st

st.title("👤 About the Developer")

# ---- PROFILE SECTION ----
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/ihenacho_image.jpeg", width=200)

with col2:
    st.markdown("""
    ### Moses Ihenacho  
    **AI/ML Product Manager | Machine Learning Specialist**

    I specialize in building AI-driven decision systems for supply chain,
    finance, and enterprise optimization. Passionate about intelligent
    automation and predictive analytics.
    """)

st.divider()

# ---- CERTIFICATIONS SECTION ----
st.subheader("🎓 Professional Certifications")

cert_col1, cert_col2, cert_col3, cert_col4, cert_col5 = st.columns(5)

with cert_col1:
    st.image("assets/certificates/cert1.jpg", use_container_width=True)
    st.caption("Master of ChatGPT")

with cert_col2:
    st.image("assets/certificates/cert2.jpg", use_container_width=True)
    st.caption("Master of CLAUDE")

with cert_col3:
    st.image("assets/certificates/cert3.jpg", use_container_width=True)
    st.caption("Certified AI Digital Marketer")

with cert_col4:
    st.image("assets/certificates/cert4.jpeg", use_container_width=True)
    st.caption("Introduction to Anti-Money Laundering Regulations")

with cert_col5:
    st.image("assets/certificates/cert5.jpg", use_container_width=True)
    st.caption("Managing Partnerships and Strategic Alliances")

st.divider()

# ---- SOCIAL LINKS ----
st.subheader("🌍 Connect With Me")

st.markdown(""" 
- 🔗 **LinkedIn:** https://www.linkedin.com/in/moses-ihenacho-b154a145/ 
- 🔗 **Twitter:** https://x.com/ihenachomoses?s=21&t=9o-CZlc_P6P9XQe-zPYQSw 
""")

st.success("Building Intelligent Systems for Real-World Impact 🚀")
# pages/Provider_Search.py
import streamlit as st
import pandas as pd
from utils import switch_page

st.title("My Medical Gateway")
st.subheader("Find Providers")

st.write("Search for providers by specialty.")

# Specialty selectbox (single select)
specialties = [
    'Arthroscopy', 
    'Foot and ankle surgery', 
    'Hip replacement surgery', 
    'Joint fusion', 
    'Knee replacement surgery'
]
selected_specialty = st.selectbox('Specialty', specialties)

if st.button('Continue to Patient Profile'):
    if not selected_specialty:
        st.warning("Please select a specialty.")
    else:
        st.session_state.selected_specialty = selected_specialty
        switch_page("Patient")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>
""", unsafe_allow_html=True)

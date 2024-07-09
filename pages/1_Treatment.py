# pages/Provider_Search.py
import streamlit as st
import pandas as pd
from utils import switch_page

# Inject CSS for custom styling
st.markdown("""
    <style>
        .stSelectbox div[data-baseweb="select"] {
            width: 200px;  /* Adjust the width as needed */
        }
    </style>
""", unsafe_allow_html=True)

st.image("img/mmg-logo-small.png", width=200)
st.title("My Medical Gateway")
st.subheader("Get a quote for your orthpaedic treatment")

st.write("My Medical Gateway finds treatment for you in a quality private hospital of your choice in the EU, at a price you can afford.")

st.subheader("Your treatment")

st.write("What treatment do you require?")

# Specialty selectbox (single select)
specialties = [
    'Arthroscopy', 
    'Foot and ankle surgery', 
    'Hip replacement surgery', 
    'Joint fusion', 
    'Knee replacement surgery'
]
selected_specialty = st.selectbox('Specialty', specialties)

if st.button('Get Quote'):
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

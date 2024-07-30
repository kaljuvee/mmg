# pages/Provider_Search.py
import streamlit as st
import pandas as pd
from utils import switch_page
from utils import load_css

# Inject CSS for custom styling
st.markdown("""
    <style>
        .stSelectbox div[data-baseweb="select"] {
            width: 200px;  /* Adjust the width as needed */
        }
    </style>
""", unsafe_allow_html=True)

load_css("html/progress.css")

st.image("img/mmg-logo-small.png", width=200)
st.title("My Medical Gateway")

# Render the progress bar
st.markdown("""
    <div class="progress-container">
        <div class="progress-step active">
            <div class="circle">1</div>
            <div class="label">Treatment</div>
        </div>
        <div class="progress-step-line"></div>
        <div class="progress-step">
            <div class="circle">2</div>
            <div class="label">Patient</div>
        </div>
        <div class="progress-step-line"></div>
        <div class="progress-step">
            <div class="circle">3</div>
            <div class="label">View Quote</div>
        </div>
        <div class="progress-step-line"></div>
        <div class="progress-step">
            <div class="circle">4</div>
            <div class="label">Payment</div>
        </div>
        <div class="progress-step-line"></div>
        <div class="progress-step">
            <div class="circle">5</div>
            <div class="label">Confirmation</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.subheader("Get a quote for your opthalmology treatment.")

st.write("My Medical Gateway finds treatment for you in a quality private hospital of your choice in the EU, at a price you can afford.")

st.subheader("Your treatment")

st.write("What treatment do you require?")

# Specialty selectbox (single select)
specialties = [
    'Cataract Surgery', 
    'Glaucoma Treatment', 
    'Retina and Vitreous Surgery', 
    'Corneal Transplantation', 
    'Refractive Surgery'
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
    <p>My Medical Gateway International Limited</p>
</div>

""", unsafe_allow_html=True)
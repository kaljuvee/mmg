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
        <div class="progress-step-line">
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
        <div class="progress-step active"></div>
        <div class="progress-step">
            <div class="circle">5</div>
            <div class="label">Confirmation</div>
        </div>
    </div>
""", unsafe_allow_html=True)
st.subheader("Payment")
# Retrieve email from session state
email = st.session_state.get('email', '')

if email:
    st.write(f"Your payment has been successfully processed. Thank you for choosing My Medical Gateway! An email was sent to {email}.")
else:
    st.write("Your payment has been successfully processed. Thank you for choosing My Medical Gateway!")

st.write("If you are happy with the quote,  please visit My Medical Gateway to upload addtional information.")

if st.button('Book Consultation'):
    switch_page("Book_Consultation")

if st.button('Visit MMG'):
    switch_page("Documents")

st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>

""", unsafe_allow_html=True)
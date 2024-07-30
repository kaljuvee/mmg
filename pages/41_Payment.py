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
        <div class="progress-step completed">
            <div class="circle">1</div>
            <div class="label">Treatment</div>
        </div>
        <div class="progress-step-line completed"></div>
        <div class="progress-step completed">
            <div class="circle">2</div>
            <div class="label">Patient</div>
        </div>
        <div class="progress-step-line completed"></div>
        <div class="progress-step completed">
            <div class="circle">3</div>
            <div class="label">View Quote</div>
        </div>
        <div class="progress-step-line completed"></div>
        <div class="progress-step active">
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

st.subheader("Payment")


# Retrieve the first name, last name, and address from session state
first_name = st.session_state.get('first_name', '')
last_name = st.session_state.get('last_name', '')
address = st.session_state.get('address', '')

card_name = f"{first_name} {last_name}"

# Prepopulate cardholder name and billing address fields if not already set
if 'card_name' not in st.session_state:
    st.session_state.card_name = f"{first_name} {last_name}"
if 'card_address' not in st.session_state:
    st.session_state.card_address = address
if 'card_number' not in st.session_state:
    st.session_state.card_number = ''

# Display debug information
#st.write(f"Address: {address}")
#st.write(f"Card Name: {st.session_state.card_name}")

# Input fields
st.session_state.card_name = st.text_input('Cardholder Name:', st.session_state.card_name)
st.session_state.card_address = st.text_input('Billing Address:', st.session_state.card_address)
st.session_state.card_number = st.text_input('Card Number:', st.session_state.card_number)


if st.button('Submit Payment'):
    # Here you would typically process the payment
    # For this example, we're just showing a success message
    st.success("Payment submitted successfully!")
    switch_page("Confirmation")

if st.button('Back to Quote Page'):
    switch_page("Quote Page")

st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>

""", unsafe_allow_html=True)
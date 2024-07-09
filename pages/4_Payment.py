# pages/4_Payment.py
import streamlit as st
from utils import switch_page

st.title("My Medical Gateway")
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

# Input fields
st.session_state.card_name = st.text_input('Cardholder Name:', card_name)
st.session_state.card_address = st.text_input('Billing Address:', address)
st.session_state.card_number = st.text_input('Card Number:', st.session_state.card_number)

if st.button('Submit Payment'):
    # Here you would typically process the payment
    # For this example, we're just showing a success message
    st.success("Payment submitted successfully!")
    switch_page("Confirmation")

if st.button('Back to Quote Page'):
    switch_page("Quote Page")

# pages/5_Confirmation.py
import streamlit as st
from utils import switch_page

st.title("My Medical Gateway")
st.subheader("Confirmation")

# Retrieve email from session state
email = st.session_state.get('email', 'your email')

st.write(f"Your payment has been successfully processed. Thank you for choosing My Medical Gateway! An email was sent to {email}.")

if st.button('Back to Home'):
    switch_page("Home")


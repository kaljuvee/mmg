# pages/5_Confirmation.py
import streamlit as st
from utils import switch_page

st.image("img/mmg-logo-small.png", width=200)
st.title("My Medical Gateway")
st.subheader("Confirmation")

# Retrieve email from session state
email = st.session_state.get('email', '')

if email:
    st.write(f"Your payment has been successfully processed. Thank you for choosing My Medical Gateway! An email was sent to {email}.")
else:
    st.write("Your payment has been successfully processed. Thank you for choosing My Medical Gateway!")

st.write("If you are happy with the quote,  please visit My Medical Gateway to upload addtional information.")

if st.button('Visit MMG'):
    switch_page("Documents")
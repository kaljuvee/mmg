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

if st.button('Book Consultation'):
    switch_page("Book_Consultation")

if st.button('Visit MMG'):
    switch_page("Documents")

st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited (Company no. 1234567) is Registered in RAK IIC at Registered Office
    address G03 Emaar Building 3, Emaar Business Park, Dubai, UAE.</p>
</div>

""", unsafe_allow_html=True)
# pages/Book_Consultation.py
import streamlit as st
import datetime
from utils import switch_page

# Sample function to load provider name (In a real scenario, you'd fetch this data from a database or another source)
def load_provider_name():
    # This is a placeholder for actual provider data
    provider_name = "Dr. John Doe"
    return provider_name

# Load the provider name
provider_name = load_provider_name()

# Page title and header
st.image("img/mmg-logo-small.png", width=200)
st.title("Book Consultation")


# Provider name section
st.subheader(f"Provider: {provider_name}")

# Calendar widget to select a consultation date
st.write("Select a date for your consultation:")
selected_date = st.date_input("Consultation Date", datetime.date.today())

# Confirm booking button
if st.button("Confirm Booking"):
    st.success(f"Consultation booked with {provider_name} on {selected_date}")

# Navigation buttons
if st.button('Back to Clinic Details'):
    switch_page("Clinic_Details")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>

""", unsafe_allow_html=True)

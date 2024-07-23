# pages/Clinic_Details.py
import streamlit as st
import pandas as pd
from utils import switch_page

# Sample function to load provider details (In a real scenario, you'd fetch this data from a database or another source)
def load_provider_details():
    # This is a placeholder for actual provider data
    provider_details = {
        "Doctor": "Dr. John Doe",
        "ClinicName": "Ortho Center",
        "Address": "123 Main St",
        "City": "Riga",
        "Country": "Latvia",
        "Specialty": "Orthopedics",
        "SubSpecialty": "Arthroscopy",
        "Quote(EUR)": "1500",
        "ReviewStars": "img/5-star.PNG"  # Path to the image of stars for review
    }
    return provider_details

# Load the provider details
provider = load_provider_details()

st.image("img/mmg-logo-small.png", width=200)
# Page title and header
st.title("Clinic Details")


# Clinic details section
st.subheader(f"Doctor: {provider['Doctor']}")
st.write(f"**Clinic Name:** {provider['ClinicName']}")
st.write(f"**Address:** {provider['Address']}")
st.write(f"**City:** {provider['City']}")
st.write(f"**Country:** {provider['Country']}")
st.write(f"**Specialty:** {provider['Specialty']}")
st.write(f"**SubSpecialty:** {provider['SubSpecialty']}")
st.write(f"**Quote(EUR):** {provider['Quote(EUR)']}")
st.write(f"**riority waiting time (average):** 2 weeks")
st.write(f"**Regular waiting time (average):** 8 weeks")

# Review stars image
st.image(provider['ReviewStars'], width=100, caption="Review Stars")

# Navigation buttons
if st.button('Proceed to Payment'):
    st.session_state.selected_provider = provider
    switch_page("Payment")

if st.button('Back to Quotes'):
    switch_page("Quote")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited (Company no. 1234567) is Registered in RAK IIC at Registered Office
    address G03 Emaar Building 3, Emaar Business Park, Dubai, UAE.</p>
</div>

""", unsafe_allow_html=True)

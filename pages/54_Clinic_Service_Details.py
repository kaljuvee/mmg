import streamlit as st
from utils import switch_page

# Set page title and icon
# st.set_page_config(page_title='My Medical Gateway', page_icon='📝')

st.image("img/mmg-logo-small.png", width=200)

# Page title
st.title("Clinic Service Details")

# Input fields for Clinic Service Details
service_name = st.text_input('Service Name')
service_description = st.text_area('Service Description')
service_price = st.number_input('Service Price', min_value=0.0, format="%f")
service_details = st.text_area('Service Details')
patient_requirements = st.text_area('Patient Requirements')
additional_comments = st.text_area('Additional Comments')

# Submit button
if st.button('Submit Service Details'):
    # Here you would typically process the form data
    st.write("Service Name:", service_name)
    st.write("Service Description:", service_description)
    st.write("Service Price:", service_price)
    st.write("Service Details:", service_details)
    st.write("Patient Requirements:", patient_requirements)
    st.write("Additional Comments:", additional_comments)

    st.success("Service details submitted successfully!")

# Disclaimer
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited</p>
</div>
""", unsafe_allow_html=True)

if st.button('Next - Review'):
    switch_page("Review")

if st.button('Back - Clinic Signup'):
    switch_page("Clinic_Signup")

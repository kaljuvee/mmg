import streamlit as st
import pandas as pd
from utils import switch_page

# Dummy data for the providers
data = {
    "ClinicName": ["Ortho Center"],
    "Address": ["123 Main St"],
    "City": ["Riga"],
    "Country": ["Latvia"],
    "Specialty": ["Orthopedics"],
    "SubSpecialty": ["Arthroscopy"],
    "Quote (EUR)": ["500"]
}

# Create a DataFrame
df = pd.DataFrame(data)

st.image("img/mmg-logo-small.png", width=200)
# Streamlit app
st.title("My Medical Gateway")
st.subheader("Your Account")

# Display patient name if available in session state
first_name = st.session_state.get('first_name', '')
st.write(f"Below is your account information. You can edit the fields below if needed, then click 'Save' to update your information.")

# Display the DataFrame
st.write("Your bookings:")
st.dataframe(df)

# Editable fields
st.subheader("Contact Information:")
st.session_state.first_name = st.text_input('First name:', st.session_state.first_name)
st.session_state.last_name = st.text_input('Last name:', st.session_state.last_name)
st.session_state.email = st.text_input('Email:', st.session_state.email)
st.session_state.phone = st.text_input('Phone:', st.session_state.phone)
st.session_state.address = st.text_input('Address:', st.session_state.address)

st.subheader("Additional Information:")
st.session_state.problem_description = st.text_area('Additional comments (optional):', st.session_state.problem_description)
st.session_state.insurance = st.text_input('Insurance (if any):', st.session_state.insurance)
st.session_state.travel_companion = st.text_input('Travel companion (if applicable):', st.session_state.travel_companion)
st.session_state.next_of_kin = st.text_input('Next of kin (optional):', st.session_state.next_of_kin)
st.session_state.surgery_type = st.text_input('Surgery type:', st.session_state.surgery_type)
st.session_state.indicative_duration = st.selectbox('Indicative appointment time:', ['0-4 weeks', '4-8 weeks', '8-12 weeks', 'More than 12 weeks'], index=['0-4 weeks', '4-8 weeks', '8-12 weeks', 'More than 12 weeks'].index(st.session_state.indicative_duration) if 'indicative_duration' in st.session_state else 0)
st.session_state.financing_required = st.checkbox('Financing required', st.session_state.financing_required)

# Save button
if st.button('Save'):
    st.success("Information updated successfully!")

# Save button
if st.button('Home'):
    st.success("Home")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>
""", unsafe_allow_html=True)

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

st.subheader("Provider Information Requirements:")
st.session_state.problem_description = st.text_area(
    'What is the underlying diagnosis?',
    st.session_state.problem_description,
    help="Understanding the patient’s specific problem."
)
st.session_state.surgery_type = st.text_input(
    'What is the proposed / requested procedure?',
    st.session_state.surgery_type,
    help="Knowing what the specific fix required is e.g., repair vs replacement."
)
st.session_state.validated = st.selectbox(
    'Has this been validated by a medical professional?',
    ['Yes', 'No'],
    index=0 if st.session_state.validated == 'Yes' else 1,
    help="Clarification that this is the correct course of action by a medical professional."
)
st.session_state.medical_history = st.text_area(
    'Medical history:',
    st.session_state.medical_history,
    help="Additional medical problems that the anaesthetists will need to know about e.g., heart disease, diabetes etc., regarding the safety of general anaesthesia / factors that may interfere with successful operation."
)
st.session_state.diagnostics_information = st.text_area(
    'Diagnostics information:',
    st.session_state.diagnostics_information,
    help="Latest results e.g., X-rays / Scans and blood tests e.g., renal function."
)

# Save button
if st.button('Save'):
    st.success("Information updated successfully!")

# Home button
if st.button('Home'):
    switch_page("Home")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>
""", unsafe_allow_html=True)

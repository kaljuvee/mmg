import streamlit as st
from utils import switch_page

# Set page title and icon
#st.set_page_config(page_title='My Medical Gateway', page_icon='👤')

st.image("img/mmg-logo-small.png", width=200)

# Specialty list
specialties = [
    'Arthroscopy', 
    'Foot and ankle surgery', 
    'Hip replacement surgery', 
    'Joint fusion', 
    'Knee replacement surgery'
]

# Page title
st.title("Clinic Signup")

# Input fields
clinic_name = st.text_input('Name of Clinic')
contact_name = st.text_input('Contact Name')
address = st.text_input('Address')
accreditation = st.text_input('Accreditation')

# File uploader for documents
uploaded_files = st.file_uploader("Upload Documents", accept_multiple_files=True)

# Specialty selectbox
selected_specialty = st.selectbox('Specialty', specialties)

# Submit button
if st.button('Submit'):
    # Here you would typically process the form data
    st.write("Clinic Name:", clinic_name)
    st.write("Contact Name:", contact_name)
    st.write("Address:", address)
    st.write("Accreditation:", accreditation)
    st.write("Specialty:", selected_specialty)
    st.write("Uploaded Documents:", [file.name for file in uploaded_files])

    st.success("Clinic information submitted successfully!")

# Disclaimer
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited (Company no. 1234567) is Registered in RAK IIC at Registered Office
    address G03 Emaar Building 3, Emaar Business Park, Dubai, UAE.</p>
</div>
""", unsafe_allow_html=True)

if st.button('Next - Service Details'):
    switch_page("Clinic_Service_Details")

if st.button('Back to Home'):
    switch_page("Home")
import streamlit as st
from utils import switch_page

# Set page title and icon
# st.set_page_config(page_title='My Medical Gateway', page_icon='🔧')

st.image("img/mmg-logo-small.png", width=200)

# Page title
st.title("Admin Dashboard")

# Section for Patients
st.header("Patients")

# Search box for Patients
patient_search = st.text_input("Search Patients")

# Button to search
if st.button("Search Patients"):
    st.write(f"Searching for patients with name: {patient_search}")

# Button to add new Patient
if st.button("Add New Patient"):
    st.write("Form to add a new patient will go here")
    # Input fields for new patient
    new_patient_name = st.text_input('Patient Name')
    new_patient_email = st.text_input('Patient Email')
    new_patient_phone = st.text_input('Patient Phone')
    
    if st.button('Submit Patient'):
        st.write(f"New patient {new_patient_name} added successfully!")
        
st.write("---")

# Section for Clinics
st.header("Clinics")

# Search box for Clinics
clinic_search = st.text_input("Search Clinics")

# Button to search
if st.button("Search Clinics"):
    st.write(f"Searching for clinics with name: {clinic_search}")

# Button to add new Clinic
if st.button("Add New Clinic"):
    st.write("Form to add a new clinic will go here")
    # Input fields for new clinic
    new_clinic_name = st.text_input('Clinic Name')
    new_clinic_address = st.text_input('Clinic Address')
    new_clinic_specialty = st.text_input('Clinic Specialty')
    
    if st.button('Submit Clinic'):
        st.write(f"New clinic {new_clinic_name} added successfully!")

st.write("---")

# Section for Surgeons
st.header("Surgeons")

# Search box for Surgeons
surgeon_search = st.text_input("Search Surgeons")

# Button to search
if st.button("Search Surgeons"):
    st.write(f"Searching for surgeons with name: {surgeon_search}")

# Button to add new Surgeon
if st.button("Add New Surgeon"):
    st.write("Form to add a new surgeon will go here")
    # Input fields for new surgeon
    new_surgeon_name = st.text_input('Surgeon Name')
    new_surgeon_specialty = st.text_input('Surgeon Specialty')
    new_surgeon_clinic = st.text_input('Surgeon Clinic')
    
    if st.button('Submit Surgeon'):
        st.write(f"New surgeon {new_surgeon_name} added successfully!")

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

if st.button('Back to Home'):
    switch_page("Home")

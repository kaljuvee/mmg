import streamlit as st
from utils import switch_page

# Set page title and icon
# st.set_page_config(page_title='My Medical Gateway', page_icon='✅')

st.image("img/mmg-logo-small.png", width=200)

# Page title
st.title("Admin Approvals")

# Section for Patients
st.header("Patients Status")

# Sample data for patients with their statuses
patients_data = [
    {"name": "Alice Johnson", "status": "Pending"},
    {"name": "Bob Smith", "status": "Approved"},
    {"name": "Charlie Brown", "status": "Pending"},
]

# Display patients and their statuses with Approve/Revoke buttons
for patient in patients_data:
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        st.write(patient["name"])
    with col2:
        st.write(patient["status"])
    with col3:
        if patient["status"] == "Pending":
            if st.button(f"Approve", key=f"approve_{patient['name']}"):
                patient["status"] = "Approved"
                st.success(f"{patient['name']} approved.")
        else:
            if st.button(f"Revoke", key=f"revoke_{patient['name']}"):
                patient["status"] = "Pending"
                st.warning(f"{patient['name']} revoked.")

st.write("---")

# Section for Clinics
st.header("Clinics Status")

# Sample data for clinics with their statuses
clinics_data = [
    {"name": "XYZ Clinic", "status": "Pending"},
    {"name": "ABC Clinic", "status": "Approved"},
    {"name": "123 Clinic", "status": "Pending"},
]

# Display clinics and their statuses with Approve/Revoke buttons
for clinic in clinics_data:
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        st.write(clinic["name"])
    with col2:
        st.write(clinic["status"])
    with col3:
        if clinic["status"] == "Pending":
            if st.button(f"Approve", key=f"approve_{clinic['name']}"):
                clinic["status"] = "Approved"
                st.success(f"{clinic['name']} approved.")
        else:
            if st.button(f"Revoke", key=f"revoke_{clinic['name']}"):
                clinic["status"] = "Pending"
                st.warning(f"{clinic['name']} revoked.")

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

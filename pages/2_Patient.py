import streamlit as st
from utils import switch_page

# Inject CSS for custom styling
st.markdown("""
    <style>
        .stSelectbox div[data-baseweb="select"] {
            width: 200px;  /* Adjust the width as needed */
        }
    </style>
""", unsafe_allow_html=True)

st.image("img/mmg-logo-small.png", width=200)
# Page title
st.title("My Medical Gateway")
st.subheader("Patient Profile:")

# Initialize session state variables if they don't exist
if 'first_name' not in st.session_state:
    st.session_state.first_name = ''
if 'last_name' not in st.session_state:
    st.session_state.last_name = ''
if 'email' not in st.session_state:
    st.session_state.email = ''
if 'phone' not in st.session_state:
    st.session_state.phone = ''
if 'address' not in st.session_state:
    st.session_state.address = ''
if 'problem_description' not in st.session_state:
    st.session_state.problem_description = ''
if 'insurance' not in st.session_state:
    st.session_state.insurance = ''
if 'travel_companion' not in st.session_state:
    st.session_state.travel_companion = ''
if 'next_of_kin' not in st.session_state:
    st.session_state.next_of_kin = ''
if 'surgery_type' not in st.session_state:
    st.session_state.surgery_type = ''
if 'indicative_duration' not in st.session_state:
    st.session_state.indicative_duration = ''
if 'financing_required' not in st.session_state:
    st.session_state.financing_required = False

# Input fields
st.session_state.first_name = st.text_input('First name:', st.session_state.first_name)
st.session_state.last_name = st.text_input('Last name:', st.session_state.last_name)
st.session_state.email = st.text_input('Email:', st.session_state.email)
st.session_state.phone = st.text_input('Phone:', st.session_state.phone)
st.session_state.address = st.text_input('Address:', st.session_state.address)
st.session_state.problem_description = st.text_area('Additional comments (optional):', st.session_state.problem_description)
st.session_state.insurance = st.text_input('Insurance (if any):', st.session_state.insurance)
st.session_state.travel_companion = st.text_input('Travel companion (if applicable):', st.session_state.travel_companion)
st.session_state.next_of_kin = st.text_input('Next of kin (optional):', st.session_state.next_of_kin)
st.session_state.surgery_type = st.text_input('Surgery type:', st.session_state.surgery_type)
st.session_state.indicative_duration = st.selectbox('Indicative appointment time:', ['0-4 weeks', '4-8 weeks', '8-12 weeks', 'More than 12 weeks'])
st.session_state.financing_required = st.checkbox('Financing required', st.session_state.financing_required)

if st.button('See Quote'):
    # Here you would typically save the profile data
    # For this example, we're just navigating to the next page
    switch_page("Quote")

if st.button('Back to Treatment'):
    switch_page("Treatment")

st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited (Company no. 1234567) is Registered in RAK IIC at Registered Office
    address G03 Emaar Building 3, Emaar Business Park, Dubai, UAE.</p>
</div>
""", unsafe_allow_html=True)

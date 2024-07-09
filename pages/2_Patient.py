import streamlit as st
from utils import switch_page

# Set page title and icon
#st.set_page_config(page_title='My Medical Gateway', page_icon='👤')

# Page title
st.title("My Medical Gateway")
st.subheader("Create Profile")

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

# Input fields
st.session_state.first_name = st.text_input('First name:', st.session_state.first_name)
st.session_state.last_name = st.text_input('Last name:', st.session_state.last_name)
st.session_state.email = st.text_input('Email:', st.session_state.email)
st.session_state.phone = st.text_input('Phone:', st.session_state.phone)
st.session_state.address = st.text_input('Address:', st.session_state.address)
st.session_state.problem_description = st.text_area('Additional comments (optional):', st.session_state.problem_description)
st.session_state.insurance = st.text_input('Insurance (if any):', st.session_state.insurance)

if st.button('See Quote'):
    # Here you would typically save the profile data
    # For this example, we're just navigating to the next page
    switch_page("Quote")

if st.button('Back to Treatment'):
    switch_page("Orthopedics_Treatment")

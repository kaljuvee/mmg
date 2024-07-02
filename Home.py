import streamlit as st

st.title("My Medical Gateway - MVP")

st.markdown("""
# Overview

This will be replaced by the actual landing page but the current site map:
            
## Patient
- **Create profile** - patients sign up and create a profile including name, contact info, some comments on medical history, insurance information and surgery preferences.
- **Search for providers** - patients can search by (i) procedures, (ii) providers, (iii) cities, among others, or they can browse the top procedures and destinations.
                       
""")

# Set page title and icon
st.set_page_config(page_title='My Medical Gateway', page_icon='👤')

# Page navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Create Profile", "Upload Documents"])

if page == "Create Profile":
    st.session_state.page = "Create_Profile"
    st.experimental_rerun()
elif page == "Upload Documents":
    st.session_state.page = "Upload_Documents"
    st.experimental_rerun()

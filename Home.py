import streamlit as st
import sys
import os

from utils import switch_page

# Set page title and icon
st.set_page_config(page_title='My Medical Gateway', page_icon='👤')

st.title("My Medical Gateway")
st.subheader("Overview")

st.markdown("""

This will be replaced by the actual landing page but the current site map:
            
## Patient
- **Create profile** - patients sign up and create a profile including name, contact info, some comments on medical history, insurance information and surgery preferences.
- **Search for providers** - patients can search by (i) procedures, (ii) providers, (iii) cities, among others, or they can browse the top procedures and destinations.
                       
""")

if st.button('Create Profile'):
    switch_page("Create Profile")

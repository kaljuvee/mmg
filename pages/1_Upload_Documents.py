import streamlit as st
import os
from utils import switch_page

# Set page title and icon
#st.set_page_config(page_title='My Medical Gateway', page_icon='👤')

# Instructions
st.title("Document Upload")

st.write("""
    Please upload any relevant documents on your medical history and previous tests such as X-Rays and other medical records. 
    If you are unable to upload them here, please email them to us at documents@mymedicalgateway.com.
""")

# Function to save uploaded files
def save_uploaded_file(uploaded_file):
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return st.success(f"Saved file : {uploaded_file.name}")

# Create 'uploads' directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# File uploader
uploaded_files = st.file_uploader("Upload your medical documents", type=["pdf", "docx", "png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        save_uploaded_file(uploaded_file)

if st.button('Back to Profile'):
    switch_page("Create Profile")

if st.button('Next - Provider Search'):
    switch_page("Provider Search")
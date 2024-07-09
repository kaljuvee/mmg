# pages/Provider_Search.py
import streamlit as st
import pandas as pd
from utils import switch_page

def find_providers(specialty):
    # Read the CSV file
    df = pd.read_csv('providers.csv')
    
    # Filter based on selected specialty
    filtered_df = df[df['SubSpecialty'] == specialty]
    
    return filtered_df

st.title("My Medical Gateway")
st.subheader("Find Providers")

st.write("Search for providers by specialty.")

# Specialty selectbox (single select)
specialties = [
    'Arthroscopy', 
    'Foot and ankle surgery', 
    'Hip replacement surgery', 
    'Joint fusion', 
    'Knee replacement surgery'
]
selected_specialty = st.selectbox('Specialty', specialties)

# Search button and functionality
if st.button('Search Providers'):
    if not selected_specialty:
        st.warning("Please select a specialty.")
    else:
        st.write(f"Searching for providers specializing in {selected_specialty}.")
        results = find_providers(selected_specialty)
        
        if results.empty:
            st.info("No providers found matching your criteria.")
        else:
            st.success(f"Found {len(results)} provider(s) matching your criteria.")
            st.dataframe(results)

# Navigation buttons
if st.button('Back to Document Upload'):
    switch_page("Upload Documents")

if st.button('Back to Home'):
    switch_page("Home")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>
""", unsafe_allow_html=True)

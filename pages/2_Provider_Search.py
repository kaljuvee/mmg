# pages/Provider_Search.py
import streamlit as st
import pandas as pd
from utils import switch_page

def find_providers(specialties, locations):
    # Read the CSV file
    df = pd.read_csv('providers.csv')
    
    # Filter based on selected specialties and locations
    mask = df['Specialty'].isin(specialties) & df['Country'].isin(locations)
    filtered_df = df[mask]
    
    return filtered_df


st.title("My Medical Gateway")
st.subheader("Find Providers")

st.write("Search for providers by specialty and location.")

# Specialty multiselect
specialties = ['Orthopedics', 'Gynecology', 'Ophthalmology', 'Other']
selected_specialties = st.multiselect('Specialty', specialties)

# Location multiselect
locations = ['Latvia', 'Lithuania', 'Romania', 'France', 'Spain', 'Turkey', 'Poland', 'Hungary']
selected_locations = st.multiselect('Location', locations)

# Search button and functionality
if st.button('Search Providers'):
    if not selected_specialties or not selected_locations:
        st.warning("Please select at least one specialty and one location.")
    else:
        st.write(f"Searching for providers in {', '.join(selected_locations)} specializing in {', '.join(selected_specialties)}")
        results = find_providers(selected_specialties, selected_locations)
        
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
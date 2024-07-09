# pages/3_Quote_Page.py
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
st.subheader("Quote Page")

st.write("Here are the providers for your selected specialty:")

# Retrieve the selected specialty from session state
selected_specialty = st.session_state.get('selected_specialty', None)

if selected_specialty:
    results = find_providers(selected_specialty)
    
    if results.empty:
        st.info("No providers found matching your criteria.")
    else:
        st.success(f"Found {len(results)} provider(s) matching your criteria.")
        st.dataframe(results)
else:
    st.warning("No specialty selected. Please go back and select a specialty.")

# Navigation buttons
if st.button('Proceed to Payment'):
    switch_page("Payment")

if st.button('Back'):
    switch_page("Patient")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
</div>
""", unsafe_allow_html=True)

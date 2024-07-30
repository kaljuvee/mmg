import streamlit as st
import pandas as pd
import plotly.express as px
from utils import switch_page

# Set page title and icon
# st.set_page_config(page_title='My Medical Gateway', page_icon='✅')

st.image("img/mmg-logo-small.png", width=200)

# Page title
st.title("Admin NHS Waiting List")
# Load the CSV data
csv_file_path = 'data/orthopaedic_1.csv'
data = pd.read_csv(csv_file_path)

# Define the column names (you may need to adjust these based on your CSV structure)
data.columns = ['Hospital', 'First Outpatient Appointment', 'Treatment']

# Melt the dataframe to long format for easier plotting with plotly express
data_melted = data.melt(id_vars='Hospital', value_vars=['First Outpatient Appointment', 'Treatment'],
                        var_name='Type', value_name='Average Waiting Time (weeks)')

# Streamlit app
st.title("Admin - Analytics - NHS Waiting List")

st.write("""
         
            This page shows the average waiting times for outpatient appointments and treatments across different hospitals.
             The data is based on the NHS waiting list data for orthopaedic treatments.
         """)
 # Add a selection box
specialty = st.selectbox(
    "Select Specialty",
    ["Orthopaedics", "Gynaecology", "Ophthalmology"]
)

# Add a button as a placeholder
if st.button("Show"):
    st.write("Button pressed but no action defined yet.")

# Create the bar chart using Plotly Express
fig = px.bar(data_melted, x='Average Waiting Time (weeks)', y='Hospital', color='Type', orientation='h',
             title='Average Waiting Times for Outpatient Appointments and Treatments',
             labels={'Average Waiting Time (weeks)': 'Average Waiting Time (weeks)', 'Hospital': 'Hospital'})

# Display the plot in Streamlit
st.plotly_chart(fig)

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
import streamlit as st
from utils import switch_page
from pathlib import Path

# Set up the page configuration
st.set_page_config(page_title="My Medical Gateway", layout="wide")

# Function to load CSS from a file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
load_css("html/styles.css")

# Sidebar navigation
pages = {
    "Home": "Home",
    "Orthopaedics": "pages/0_Orthopaedics.py",
    "Treatment": "pages/1_Treatment.py",
    "Patient": "pages/2_Patient.py",
    "Quote": "pages/3_Quote.py",
    "Payment": "pages/4_Payment.py",
    "Confirmation": "pages/5_Confirmation.py",
    "Book Consultation": "pages/6_Book_Consultation.py",
    "My Account": "pages/8_My_Account.py",
    "Documents": "pages/9_Documents.py",
    "Registration": "pages/10_Registration.py",
    "FAQ": "pages/11_FAQ.py",
    "Clinic Signup": "pages/21_Clinic_Signup.py",
    "Clinic Details": "pages/22_Clinic_Details.py",
    "Clinic Media Upload": "pages/23_Clinic_Media_Upload.py",
    "Clinic Service Details": "pages/24_Clinic_Service_Details.py",
    "Admin Dashboard": "pages/31_Admin_Dashboard.py",
    "Admin Approvals": "pages/32_Admin_Approvals.py",
    "Admin Analytics": "pages/34_Admin_Analytics.py",
}

page_names = list(pages.keys())
selected_page = st.sidebar.selectbox("Select a page", page_names)

if selected_page == "Home":
    # Home page content
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("img/mmg-logo-small.png", width=200)

    with col2:
        st.markdown("""
            <div class="header">
                <div class="nav" style="display: flex; align-items: center;">
                    <a href="#">Home</a>
                    <a href="#">Need Help?</a>
                    <a href="#">Chat</a>
                    <a href="#">Call us</a>
                    <a href="#">FAQs</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
        <div style="padding: 2rem;">
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="background-image: url('https://cdn.usegalileo.ai/sdxl10/e7697506-5582-4d41-8e4e-f451d9486f58.png'); background-size: cover; background-position: center; border-radius: 0.75rem; aspect-ratio: 16/9; width: 100%; max-width: 600px;"></div>
                <div style="max-width: 600px; text-align: left; margin-top: 2rem;">
                    <h1>WELCOME TO MY MEDICAL GATEWAY: IMMEDIATE, QUALITY AND AFFORDABLE HEALTHCARE</h1>
                    <p>Are you on an NHS waitlist for a hip replacement, cataracts or a hernia? Unable to afford private medical insurance? Whatever medical treatment you may need, we have got you covered in a quality private hospital in the European Union. At a price you can afford.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="category-buttons">', unsafe_allow_html=True)

    categories = st.columns(4)
    with categories[0]:
        if st.button('Orthopaedics'):
            switch_page("Orthopaedics")
    with categories[1]:
        if st.button('Ophthalmology'):
            switch_page("Orthopaedics")
    with categories[2]:
        if st.button('Gynaecology'):
            switch_page("Orthopaedics")
    with categories[3]:
        if st.button('Other'):
            switch_page("Orthopaedics")

    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Load and execute the selected page
    page_path = Path(pages[selected_page])
    with open(page_path, encoding="utf-8") as f:
        code = f.read()
    exec(code, globals())

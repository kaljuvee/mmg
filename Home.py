import streamlit as st
from utils import switch_page

# Set up the page configuration
st.set_page_config(page_title="My Medical Gateway", layout="wide")

# Function to load CSS from a file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
load_css("html/styles.css")

# Header section
st.markdown("""
    <div class="header">
        <div style="display: flex; align-items: center;">
            <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" width="32" height="32">
                <g clip-path="url(#clip0)">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M47.2426 24L24 47.2426L0.757355 24L24 0.757355L47.2426 24ZM12.2426 21H35.7574L24 9.24264L12.2426 21Z" fill="currentColor"></path>
                </g>
                <defs>
                    <clipPath id="clip0">
                        <rect width="48" height="48" fill="white"></rect>
                    </clipPath>
                </defs>
            </svg>
            <h2>My Medical Gateway</h2>
        </div>
        <div class="nav" style="margin-left: auto; display: flex; align-items: center;">
            <a href="#">Home</a>
            <a href="#">Need Help?</a>
            <a href="#">Chat</a>
            <a href="#">Call us</a>
            <a href="#">FAQs</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Navigation buttons
col1, col2 = st.columns([1, 3])
with col1:
    st.button("My MMG", key="mmg", on_click=lambda: switch_page("mmg"), use_container_width=True)
    st.button("Menu", key="menu", on_click=lambda: switch_page("menu"), use_container_width=True)

with col2:
    st.image("https://cdn.usegalileo.ai/sdxl10/e694ae8c-d71b-491c-b635-a188e726a934.png", width=40)

# Main content section
st.markdown("""
    <div style="padding: 2rem;">
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div style="background-image: url('https://cdn.usegalileo.ai/sdxl10/e7697506-5582-4d41-8e4e-f451d9486f58.png'); background-size: cover; background-position: center; border-radius: 0.75rem; aspect-ratio: 16/9; width: 100%; max-width: 600px;"></div>
            <div style="max-width: 600px; text-align: left; margin-top: 2rem;">
                <h1>WELCOME TO MY MEDICAL GATEWAY: IMMEDIATE, QUALITY AND AFFORDABLE HEALTHCARE</h1>
                <p>Are you on an NHS waitlist for a hip replacement, cataracts or a hernia? Unable to afford private medical insurance? Whatever medical treatment you may need, we have got you covered in a quality private hospital in the European Union. At a price you can afford.</p>
            </div>
            <!--div class="search-bar" style="width: 100%; max-width: 600px; margin-top: 2rem;">
                <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" fill="currentColor" viewBox="0 0 256 256">
                    <path d="M229.66,218.34l-50.07-50.06a88.11,88.11,0,1,0-11.31,11.31l50.06,50.07a8,8,0,0,0,11.32-11.32ZM40,112a72,72,0,1,1,72,72A72.08,72.08,0,0,1,40,112Z"></path>
                </svg>
                <input type="text" placeholder="What treatment do you need?" />
                <button>Search</button>
            </div-->
        </div>
    </div>
""", unsafe_allow_html=True)

# Category buttons

categories = st.columns(4)
with categories[0]:
    if st.button('Orthopedics'):
        switch_page("Orthopedics")
with categories[1]:
    if st.button('Ophthalmology'):
        switch_page("Ophthalmology")
with categories[2]:
    if st.button('Gynecology'):
        switch_page("Gynecology")
with categories[3]:
    if st.button('Other'):
        switch_page("Other")

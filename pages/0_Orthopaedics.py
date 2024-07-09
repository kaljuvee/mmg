import streamlit as st
from utils import switch_page

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
                <path d="M6 6H42L36 24L42 42H6L12 24L6 6Z" fill="currentColor"></path>
            </svg>
            <h2>My Medical Gateway</h2>
        </div>
        <div class="nav" style="margin-left: auto; display: flex; align-items: center;">
            <a href="#">Chat</a>
            <a href="#">Call us</a>
            <a href="#">FAQs</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Breadcrumb navigation
st.markdown("""
    <div class="breadcrumb">
        <a href="#">Home</a>
        <span>/</span>
        <span>Orthopedics</span>
    </div>
""", unsafe_allow_html=True)

# Main content section
# Main content section with a smaller image
st.image("https://cdn.usegalileo.ai/sdxl10/b8c60733-ed79-4d55-8c2e-1706dc4f39e3.png", width=400, caption="Orthopedics")


st.markdown("""
    <h1 class="violet-heading">Find the best treatment for you</h1>
    <p class="violet-paragraph">Orthopedic treatments. We all need healthy hip joints, knees and shoulders to get around and enjoy our daily lives. Understand your options and find high quality treatment in a private hospital, in a country of your choice, at a price that you can afford. Need finance? We've got you covered.</p>
""", unsafe_allow_html=True)

# Buttons section
col1, col2 = st.columns(2)
with col1:
    if st.button("Get a quote", key="get_quote"):
        switch_page("Treatment")
with col2:
    if st.button("Retrieve quote", key="retrieve_quote"):
        switch_page("Treatment")

# Right column with account options
st.markdown("### Already a customer?")
st.markdown("""
    <p>Log in or create a MyMMG account to make changes, view your treatment documents or start a new search. Fast and easy, no need to call.</p>
""", unsafe_allow_html=True)
if st.button("Visit My MMG", key="visit_mmg"):
    switch_page("My_MMG")

st.markdown("### New to My Medical Gateway?")
st.markdown("""
    <p>Start your journey with us, get a quote for your treatment or pick up where you left off. Online or over the phone, we look forward to welcoming you.</p>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    if st.button("Get a quote", key="get_quote_2"):
        switch_page("Treatment")
with col4:
    if st.button("Retrieve quote", key="retrieve_quote_2"):
        switch_page("Treatment")

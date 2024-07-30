import streamlit as st
from utils import switch_page

# Function to load CSS from a file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
load_css("html/styles.css")

# Header section with columns
header_col1, header_col2 = st.columns([1, 3])

with header_col1:
    st.image("img/mmg-logo-small.png", width=200)

with header_col2:
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

# Breadcrumb navigation
st.markdown("""
    <div class="breadcrumb">
        <a href="#">Home</a>
        <span>/</span>
        <span>Gynaecology</span>
    </div>
""", unsafe_allow_html=True)

# Main content section
# Main content section with a smaller image
st.image("https://cdn.usegalileo.ai/sdxl10/b8c60733-ed79-4d55-8c2e-1706dc4f39e3.png", width=600, caption="Gynaecology")

st.markdown("""
    <h1 class="violet-heading">Gynaecology</h1>
    <p class="violet-paragraph">Still waiting for your hysterectomy, endometriosis treatment, or fibroid removal? No need to wait any longer. Our medical partners in the EU can treat you immediately.</p>
""", unsafe_allow_html=True)

# Buttons section
button_col1, button_col2 = st.columns([1, 1])
with button_col1:
    if st.button("Get a quote", key="get_quote"):
        switch_page("Gynaecology_Quote")
with button_col2:
    if st.button("Retrieve quote", key="retrieve_quote"):
        switch_page("Login")

# Lower content sections
st.markdown("""
    <h2 class="violet-heading">Find the best treatment for you</h2>
    <p class="violet-paragraph">Orthopaedic treatments. We all need healthy hip joints, knees and shoulders to get around and enjoy our daily lives. Understand your options and find high quality treatment in a private hospital, in a country of your choice, at a price that you can afford. Need finance? We've got you covered.</p>
""", unsafe_allow_html=True)

# Right column with account options
account_col1, account_col2 = st.columns([1, 1])

with account_col1:
    st.markdown("""
        <h2 class="violet-heading">Already a customer?</h2>
         <p class="violet-paragraph">Log in or create a MyMMG account to make changes, view your treatment documents or start a new search. Fast and easy, no need to call.</p>
    """, unsafe_allow_html=True)
    if st.button("Visit My MMG", key="visit_mmg"):
        switch_page("Login")

with account_col2:
    st.markdown("""
         <h2 class="violet-heading">New to My Medical Gateway?</h2>       
        <p class="violet-paragraph">Start your journey with us, get a quote for your treatment or pick up where you left off. Online or over the phone, we look forward to welcoming you.</p>
    """, unsafe_allow_html=True)
    quote_button_col1, quote_button_col2 = st.columns([1, 1])
    with quote_button_col1:
        if st.button("Get a quote", key="get_quote_2"):
            switch_page("Gynaecology_Quote")
    with quote_button_col2:
        if st.button("Retrieve quote", key="retrieve_quote_2"):
            switch_page("Login")

st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited</p>
</div>

""", unsafe_allow_html=True)
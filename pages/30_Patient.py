import streamlit as st
from utils import switch_page
from utils import load_css

load_css("html/progress.css")

st.image("img/mmg-logo-small.png", width=200)
st.title("My Medical Gateway")

# Render the progress bar
st.markdown("""
    <div class="progress-container">
        <div class="progress-step completed">
            <div class="circle">1</div>
            <div class="label">Treatment</div>
        </div>
        <div class="progress-step-line completed"></div>
        <div class="progress-step active">
            <div class="circle">2</div>
            <div class="label">Patient</div>
        </div>
        <div class="progress-step-line"></div>
        <div class="progress-step">
            <div class="circle">3</div>
            <div class="label">View Quote</div>
        </div>
        <div class="progress-step-line"></div>
        <div class="progress-step">
            <div class="circle">4</div>
            <div class="label">Payment</div>
        </div>
        <div class="progress-step-line"></div>
        <div class="progress-step">
            <div class="circle">5</div>
            <div class="label">Confirmation</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.header("Patient Information")

# Initialize session state variables if they don't exist
if 'first_name' not in st.session_state:
    st.session_state.first_name = ''
if 'last_name' not in st.session_state:
    st.session_state.last_name = ''
if 'email' not in st.session_state:
    st.session_state.email = ''
if 'problem' not in st.session_state:
    st.session_state.problem = ''
if 'urgency' not in st.session_state:
    st.session_state.urgency = '2-4 weeks'
if 'call_you' not in st.session_state:
    st.session_state.call_you = 'No'
if 'financing' not in st.session_state:
    st.session_state.financing = 'Self financed'
if 'preferred_countries' not in st.session_state:
    st.session_state.preferred_countries = [
        'Bulgaria', 'Croatia', 'Czech Republic', 'Hungary', 'Poland', 'Romania', 
        'Slovakia', 'Slovenia', 'Greece', 'Italy', 'Portugal', 'Spain'
    ]
if 'validated' not in st.session_state:
    st.session_state.validated = 'No'

# Input fields for primary information
st.write('Please let us know your name and your best contact email address:')
st.session_state.first_name = st.text_input('Name:', st.session_state.first_name)
st.session_state.last_name = st.text_input('Name:', st.session_state.last_name)
st.session_state.email = st.text_input('Email:', st.session_state.email)
st.session_state.problem = st.text_input('Can you tell us what the medical or surgical problem is that you need help with?', st.session_state.problem)
st.session_state.validated = st.selectbox('Has this been validated by a medical professional?', ['Yes', 'No'], index=0 if st.session_state.validated == 'Yes' else 1)
st.session_state.urgency = st.selectbox('How quickly would you like to have treatment?', ['As soon as possible - within 6 weeks', 'No rush - longer than 6 weeks'], index=0 if st.session_state.urgency == '2-4 weeks' else 1)
st.session_state.call_you = st.selectbox('Would you like us to call you:', ['Yes', 'No'], index=0 if st.session_state.call_you == 'Yes' else 1)
st.session_state.financing = st.selectbox('Do you need help with financing options?', ['Self financed', 'Health insurance', 'Monetising pension plan', 'MMG financing partners'], index=['Self financed', 'Monetising pension plan', 'MMG financing partners'].index(st.session_state.financing))

# List of countries
all_countries = [
    'Bulgaria', 'Croatia', 'Czech Republic', 'Estonia', 'Hungary', 'Latvia', 
    'Lithuania', 'Poland', 'Romania', 'Slovakia', 'Slovenia', 'Albania', 
    'Bosnia and Herzegovina', 'Greece', 'Italy', 'North Macedonia', 'Portugal', 'Spain', 'Serbia'
]

# Multiselect for preferred countries
# Name up to 3 countries
st.session_state.preferred_countries = st.multiselect(
    'Do you have a preference for the location of your treatment?', 
    options=all_countries, 
    default=[
        'Bulgaria', 'Croatia', 'Czech Republic', 'Hungary', 'Poland', 'Romania', 
        'Slovakia', 'Slovenia', 'Greece', 'Italy', 'Portugal', 'Spain'
    ]
)

st.markdown("""
**Note:** Once you have confirmed your booking, our providers may ask you for additional information on your medical history and condition before you arrive.
                   
""")

col1, col2 = st.columns(2)

with col1:
    if st.button('Submit'):
        # Handle submission logic here
        switch_page("View_Quote")

with col2:
    if st.button('Provide More Info'):
        # Optionally, handle additional information logic here
        switch_page("My_Account")

# Optional: Disclaimer or additional information
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited</p>
</div>
""", unsafe_allow_html=True)

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
if 'name' not in st.session_state:
    st.session_state.name = ''
if 'phone' not in st.session_state:
    st.session_state.phone = ''
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

# Input fields for primary information
st.session_state.name = st.text_input('Name:', st.session_state.name)
st.session_state.phone = st.text_input('Phone:', st.session_state.phone)
st.session_state.urgency = st.selectbox('How urgent / when:', ['2-4 weeks', '4 weeks or longer'], index=0 if st.session_state.urgency == '2-4 weeks' else 1)
st.session_state.call_you = st.selectbox('Would you like us to call you:', ['Yes', 'No'], index=0 if st.session_state.call_you == 'Yes' else 1)
st.session_state.financing = st.selectbox('Financing chosen:', ['Self financed', 'Monetising pension plan', 'MMG financing partners'], index=['Self financed', 'Monetising pension plan', 'MMG financing partners'].index(st.session_state.financing))

# List of countries
all_countries = [
    'Bulgaria', 'Croatia', 'Czech Republic', 'Estonia', 'Hungary', 'Latvia', 
    'Lithuania', 'Poland', 'Romania', 'Slovakia', 'Slovenia', 'Albania', 
    'Bosnia and Herzegovina', 'Greece', 'Italy', 'North Macedonia', 'Portugal', 'Spain', 'Serbia'
]

# Multiselect for preferred countries
st.session_state.preferred_countries = st.multiselect(
    'Preferred treatment countries:', 
    options=all_countries, 
    default=[
        'Bulgaria', 'Croatia', 'Czech Republic', 'Hungary', 'Poland', 'Romania', 
        'Slovakia', 'Slovenia', 'Greece', 'Italy', 'Portugal', 'Spain'
    ]
)

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

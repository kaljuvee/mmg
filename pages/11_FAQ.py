import streamlit as st
import os
from utils import switch_page

# Set page title and icon
#st.set_page_config(page_title='My Medical Gateway', page_icon='👤')

st.image("img/mmg-logo-small.png", width=200)

st.title("My Medical Gateway - FAQ")

st.header("General Information")
st.subheader("What is My Medical Gateway?")
st.write("""
My Medical Gateway is a comprehensive medical tourism application that connects patients with top-rated healthcare providers around the world. Our platform offers a seamless experience for finding, booking, and managing medical treatments abroad.
""")

st.subheader("How does My Medical Gateway work?")
st.write("""
My Medical Gateway allows users to search for medical treatments and providers, compare costs, read reviews, and book appointments. The platform also offers additional services such as travel arrangements, accommodation, and post-treatment care.
""")

st.header("Getting Started")
st.subheader("How do I sign up for My Medical Gateway?")
st.write("""
To sign up, download the My Medical Gateway app from the App Store or Google Play, and follow the on-screen instructions to create an account.
""")

st.subheader("Is My Medical Gateway free to use?")
st.write("""
Yes, signing up and using My Medical Gateway to search and compare providers is free. However, fees may apply for booking services and additional concierge services.
""")

st.header("Medical Providers and Treatments")
st.subheader("How do I find a medical provider or treatment?")
st.write("""
You can search for medical providers or treatments by entering keywords, selecting a specific treatment category, or browsing by destination. The search results can be filtered based on various criteria such as cost, rating, and location.
""")

st.subheader("Are the medical providers on My Medical Gateway certified?")
st.write("""
Yes, all medical providers listed on My Medical Gateway are thoroughly vetted and certified. We ensure that they meet international standards of care and have the necessary accreditations.
""")

st.subheader("Can I read reviews from other patients?")
st.write("""
Yes, our platform includes reviews and ratings from other patients who have used the services of the listed medical providers. These reviews can help you make an informed decision.
""")

st.header("Booking and Appointments")
st.subheader("How do I book an appointment?")
st.write("""
Once you have selected a medical provider and treatment, you can book an appointment directly through the app. You will receive a confirmation email with all the necessary details.
""")

st.subheader("Can I reschedule or cancel my appointment?")
st.write("""
Yes, you can reschedule or cancel your appointment through the app. Please refer to the provider’s cancellation policy for any potential fees or restrictions.
""")

st.header("Travel and Accommodation")
st.subheader("Does My Medical Gateway help with travel arrangements?")
st.write("""
Yes, My Medical Gateway offers services to help you arrange travel, including flights, transportation, and accommodations. You can find these options within the app after booking your treatment.
""")

st.subheader("Can I get assistance with visa requirements?")
st.write("""
Yes, we provide information and assistance with visa requirements for medical travel. Please contact our customer support for specific inquiries related to your destination.
""")

st.header("Payment and Insurance")
st.subheader("What payment methods are accepted?")
st.write("""
We accept various payment methods including credit/debit cards, bank transfers, and online payment platforms. Specific payment options will be available at the time of booking.
""")

st.subheader("Does My Medical Gateway accept insurance?")
st.write("""
Insurance acceptance varies by provider. You can check the insurance information on the provider’s profile or contact our support team for assistance.
""")

st.header("Support and Assistance")
st.subheader("How can I contact customer support?")
st.write("""
You can contact our customer support team through the app’s help center, by email at support@mymedicalgateway.com, or by calling our toll-free number.
""")

st.subheader("What should I do in case of an emergency while abroad?")
st.write("""
In case of an emergency, immediately contact local emergency services. My Medical Gateway also offers 24/7 support to assist you in urgent situations.
""")

st.header("Privacy and Security")
st.subheader("How is my personal information protected?")
st.write("""
My Medical Gateway uses advanced encryption and security protocols to protect your personal and medical information. We are committed to maintaining the highest standards of data privacy.
""")

st.subheader("Can I delete my account?")
st.write("""
Yes, you can delete your account at any time through the app’s settings. Please note that deleting your account will remove all your data from our system.
""")

st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited (Company no. 1234567) is Registered in RAK IIC at Registered Office
    address G03 Emaar Building 3, Emaar Business Park, Dubai, UAE.</p>
</div>

""", unsafe_allow_html=True)

if st.button('Back to MMG'):
    switch_page("Patient")

if st.button('Back to Quote'):
    switch_page("Quote")
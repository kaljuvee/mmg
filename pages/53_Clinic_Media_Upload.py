import streamlit as st
from utils import switch_page

# Set page title and icon
# st.set_page_config(page_title='My Medical Gateway', page_icon='📸')

st.image("img/mmg-logo-small.png", width=200)

# Page title
st.title("Upload Photos and Videos")

# Section for photo uploads
st.header("Upload Photos")
photo_1 = st.file_uploader("Upload Photo 1", type=["jpg", "jpeg", "png"], key="photo_1")
photo_2 = st.file_uploader("Upload Photo 2", type=["jpg", "jpeg", "png"], key="photo_2")
photo_3 = st.file_uploader("Upload Photo 3", type=["jpg", "jpeg", "png"], key="photo_3")

# Section for video uploads
st.header("Upload Videos")
video_1 = st.file_uploader("Upload Video 1", type=["mp4", "mov", "avi"], key="video_1")
video_2 = st.file_uploader("Upload Video 2", type=["mp4", "mov", "avi"], key="video_2")
video_3 = st.file_uploader("Upload Video 3", type=["mp4", "mov", "avi"], key="video_3")

# Submit button
if st.button('Submit'):
    st.write("Uploaded Photos:")
    if photo_1:
        st.image(photo_1, caption="Photo 1", use_column_width=True)
    if photo_2:
        st.image(photo_2, caption="Photo 2", use_column_width=True)
    if photo_3:
        st.image(photo_3, caption="Photo 3", use_column_width=True)

    st.write("Uploaded Videos:")
    if video_1:
        st.video(video_1)
    if video_2:
        st.video(video_2)
    if video_3:
        st.video(video_3)

    st.success("Photos and Videos uploaded successfully!")

# Disclaimer
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited</p>
</div>
""", unsafe_allow_html=True)

if st.button('Back - Clinic Signup'):
    switch_page("Clinic_Signup")

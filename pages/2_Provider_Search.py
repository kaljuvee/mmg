import streamlit as st

# Set page title and icon
st.set_page_config(page_title='My Medical Gateway - Provider Search', page_icon='🔍')

# Page title
st.title('Provider Search')

# Display the captured profile information
st.subheader('Your Profile Information')
st.write(f"**First Name:** {st.session_state.get('first_name', '')}")
st.write(f"**Last Name:** {st.session_state.get('last_name', '')}")
st.write(f"**Email:** {st.session_state.get('email', '')}")
st.write(f"**Phone:** {st.session_state.get('phone', '')}")
st.write(f"**Address:** {st.session_state.get('address', '')}")
st.write(f"**Problem Description:** {st.session_state.get('problem_description', '')}")
st.write(f"**Insurance:** {st.session_state.get('insurance', '')}")

# Display a message
st.info('This is the Provider Search page. You can implement the search functionality here.')

import streamlit as st
import pandas as pd
from utils import switch_page

st.image("img/mmg-logo-small.png", width=200)
st.title("My Medical Gateway")
st.subheader("Login")

# Function to save user data to a CSV file (you can use a database instead)
def save_user_data(user_data):
    user_data_df = pd.DataFrame(user_data, index=[0])
    try:
        existing_data = pd.read_csv('user_data.csv')
        updated_data = pd.concat([existing_data, user_data_df], ignore_index=True)
    except FileNotFoundError:
        updated_data = user_data_df
    updated_data.to_csv('user_data.csv', index=False)

st.title("User Portal")

# Sign In section
st.header("Sign In")
with st.form("sign_in_form"):
    sign_in_email = st.text_input("Email", key="sign_in_email")
    sign_in_password = st.text_input("Password", type="password", key="sign_in_password")
    sign_in_submitted = st.form_submit_button("Sign In")
    
    if sign_in_submitted:
        try:
            existing_data = pd.read_csv('user_data.csv')
            user = existing_data[(existing_data['Email'] == sign_in_email) & (existing_data['Password'] == sign_in_password)]
            if not user.empty:
                st.success("Sign In successful!")
                switch_page("My Account")
            else:
                st.error("Invalid email or password.")
        except FileNotFoundError:
            st.error("Could not find the user. Please sign up first.")

# Option to Sign Up
st.markdown("##")
st.markdown("Don't have an account? Sign up below:")

# Registration form
with st.form("signup_form"):
    first_name_signup = st.text_input("First Name", key="first_name_signup")
    last_name_signup = st.text_input("Last Name", key="last_name_signup")
    email_signup = st.text_input("Email", key="email_signup")
    password_signup = st.text_input("Password", type="password", key="password_signup")
    confirm_password_signup = st.text_input("Confirm Password", type="password", key="confirm_password_signup")
    
    signup_submitted = st.form_submit_button("Sign Up")

    if signup_submitted:
        if password_signup == confirm_password_signup:
            user_data_signup = {
                'First Name': first_name_signup,
                'Last Name': last_name_signup,
                'Email': email_signup,
                'Password': password_signup
            }
            save_user_data(user_data_signup)
            st.success("Sign Up successful!")
            switch_page("My Account")
        else:
            st.error("Passwords do not match.")

# pages/10_Registration.py
import streamlit as st
import pandas as pd

# Function to save user data to a CSV file (you can use a database instead)
def save_user_data(user_data):
    user_data_df = pd.DataFrame(user_data, index=[0])
    try:
        existing_data = pd.read_csv('user_data.csv')
        updated_data = pd.concat([existing_data, user_data_df], ignore_index=True)
    except FileNotFoundError:
        updated_data = user_data_df
    updated_data.to_csv('user_data.csv', index=False)

st.title("User Registration")

# Registration form
with st.form("registration_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    submitted = st.form_submit_button("Register")

    if submitted:
        if password == confirm_password:
            user_data = {
                'First Name': first_name,
                'Last Name': last_name,
                'Email': email,
                'Password': password
            }
            save_user_data(user_data)
            st.success("Registration successful!")
        else:
            st.error("Passwords do not match.")

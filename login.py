import streamlit as st
import random

st.set_page_config(page_title="Login", page_icon="🔐")

# Initialize session state variables
if 'otp' not in st.session_state:
    st.session_state.otp = None
if 'email' not in st.session_state:
    st.session_state.email = ""

st.title("🔐 Login")

# Step 1: Enter email
email = st.text_input("Enter your email:", value=st.session_state.email)
st.session_state.email = email

# Step 2: Button to send OTP
if st.button("Send OTP"):
    if email:
        st.session_state.otp = str(random.randint(100000, 999999))
        st.success(f"✅ OTP sent to {email} (for testing: {st.session_state.otp})")
    else:
        st.error("Please enter an email address")

# Step 3: Enter OTP
if st.session_state.otp is not None:
    user_otp = st.text_input("Enter OTP:")

    # Verify OTP button
    if st.button("Verify OTP"):
        if user_otp == st.session_state.otp:
            st.success("✅ Login successful!")
            # Clear OTP after successful login
            st.session_state.otp = None

            # Redirect to your app page (must be in pages folder)
            st.experimental_rerun()  # rerun app to reflect state change
            
            # Use st.session_state flag to indicate logged in
            st.session_state.logged_in = True

        else:
            st.error("❌ Invalid OTP")

# If logged in, redirect to main app page
if st.session_state.get('logged_in', False):
    # Redirect using switch_page (Streamlit 1.18+)
    st.session_state.logged_in = False  # Reset flag after redirect
    st.experimental_set_query_params() # Clear query params if any
    st.experimental_rerun()
    st.switch_page("app")  # Assumes your app page filename is 'App.py' inside 'pages'

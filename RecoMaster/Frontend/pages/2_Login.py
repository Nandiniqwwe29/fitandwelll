import base64
import streamlit as st
import pyodbc
import hashlib

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your local background image
image_path = "C:/RecoMaster/Frontend/Assets/signbg.jpg"  # Ensure this path is correct

# Base64 encode the image
base64_image = get_base64_image(image_path)

# Function to connect to the SQL Server
def init_db_connection():
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-0DS5K9U\SQLEXPRESS;'
        'DATABASE=RecoMaster;'
        'Trusted_Connection=yes;'
    )
    return connection

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to validate user login and get user data
def login_user(username, password):
    conn = init_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute('''
        SELECT id FROM users WHERE username = ? AND password = ?
    ''', (username, hashed_password))
    data = cursor.fetchone()
    conn.close()
    return data  # Return the fetched data (None if not found)

# Streamlit UI for Log In
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Add background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-position: center;
        background-size: cover;
        height: 100vh; /* Full viewport height */
        overflow: hidden; /* Hide scrollbars */
    }}
   
    .login-title {{
        text-align: center; /* Center the title */
        color: black; /* Change title color to black */
       
        font-weight: bold; /* Make the title bold */
    }}
    .signup-link {{
        text-align: center; /* Center the signup link */
        margin-top: 0px; /* Space above the link */
        font-weight: bold; /* Make text bold */
    }}
    .forgot-password {{
        text-align: center; /* Center the forgot password link */
        margin-top: 10px; /* Space above the link */
        font-weight: bold; /* Make text bold */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if not st.session_state.logged_in:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="login-title">Log In</h2>', unsafe_allow_html=True)  # Use markdown for the title

    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")

    if st.button("Log In"):
        if username and password:
            user_data = login_user(username, password)
            if user_data:
                st.session_state.logged_in = True
                st.session_state['id'] = user_data[0]  # Store user ID in session state
                st.success(f"Welcome, {username}!")
                # Optionally redirect or reload the page
                # st.experimental_rerun() 
            else:
                st.error("Invalid username or password.")
        else:
            st.error("Please fill in all fields.")

    # Place the Sign Up link next to the Log In button
    st.markdown(
        '<div class="signup-link">'
        "Don't have an account? <a href='../Signup' style='color: black;'>Sign Up here</a>"
        '</div>',
        unsafe_allow_html=True
    )

    # Add the Forgot Password link
    st.markdown(
        '<div class="forgot-password">'
        "<a href='../ForgotPassword' style='color: white;'>Forgot Password?</a>"
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)  # Close the login container

else:
    st.write("You are already logged in!")
    st.write("You can now access the Meal Recommendation page.")

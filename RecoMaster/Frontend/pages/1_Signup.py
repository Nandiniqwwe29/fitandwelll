import base64
import streamlit as st
import pyodbc
import hashlib

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your local image
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

# Function to create the table if it doesn't exist
def create_table():
    conn = init_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' AND xtype='U')
        CREATE TABLE users (
            id INT IDENTITY(1,1) PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if a user already exists
def user_exists(username):
    conn = init_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    data = cursor.fetchone()
    conn.close()
    return data is not None

# Function to add a new user
def add_user(username, email, password):
    conn = init_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute('''
        INSERT INTO users (username, email, password) 
        VALUES (?, ?, ?)
    ''', (username, email, hashed_password))
    conn.commit()
    conn.close()

# Create the table if not exists
create_table()

# Custom CSS for setting the background image and styling
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
    .title {{
        color: black; /* Change title color */
        text-align: center; /* Center title */
        margin-top: 20px; /* Optional: add space from the top */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI for Sign Up
st.markdown('<h1 class="title">Sign Up</h1>', unsafe_allow_html=True)

username = st.text_input("Enter your username")
email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")

if st.button("Sign Up"):
    if username and email and password:
        if not user_exists(username):
            add_user(username, email, password)
            st.success("Sign up successful! You can now log in.")
        else:
            st.error("Username already exists.")
    else:
        st.error("Please fill in all fields.")

# Link to the login page
st.markdown('<span class="login-link">Already have an account? <a href="../Login" style="color: white; text-decoration: underline;">Log In here</a></span>', unsafe_allow_html=True)


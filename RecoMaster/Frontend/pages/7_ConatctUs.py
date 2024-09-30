import base64
import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to get base64 encoded image
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your local background image
image_path = "C:/RecoMaster/Frontend/Assets/signbg.jpg"  # Ensure this path is correct

# Base64 encode the image
base64_image = get_base64_image(image_path)

# Set the background image and styles
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
    .center-title {{
        text-align: center; /* Center the text */
        color: black; /* Set text color to black */
        font-weight: bold; /* Bold text */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Email configuration
remail = os.getenv("email")
spassword = os.getenv("password")

# Function to send email
def send_email(sender_email, sender_name, message_content):
    # Email configuration
    receiver_email = remail  # Your email address to receive contact requests
    sender_password = spassword  # You might need to create an app password if using Gmail

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Contact Us Form: {sender_name}"

    # Email body
    body = f"Sender Name: {sender_name}\nSender Email: {sender_email}\n\nMessage:\n{message_content}"
    msg.attach(MIMEText(body, 'plain'))

    # SMTP server setup (this example uses Gmail's SMTP)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(receiver_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Streamlit Contact Form
st.markdown('<h1 class="center-title">Contact Us</h1>', unsafe_allow_html=True)

# Form for user input
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    
    submitted = st.form_submit_button("Send Message")
    
    # If the form is submitted, send the email
    if submitted:
        if name and email and message:
            success = send_email(email, name, message)
            if success:
                st.success("Your message has been sent successfully!")
        else:
            st.error("Please fill out all fields.")

import base64
import streamlit as st

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
    .center-message {{
        text-align: center; /* Center the text */
        color: black; /* Set text color to black */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to handle logout
def logout():
    if 'logged_in' in st.session_state:
        del st.session_state['logged_in']
    st.session_state.logged_in = False
    st.success("You have been logged out.")
    st.write("You have been successfully logged out.")
    st.write("Click [here](../Login) to log in again.")

# Check if user is logged in
if 'logged_in' in st.session_state and st.session_state.logged_in:
    st.markdown('<h1 class="center-title">Logout</h1>', unsafe_allow_html=True)

    if st.button("Log Out"):
        logout()
else:
    st.markdown('<h2 class="center-message">You are not logged in.</h2>', unsafe_allow_html=True)
    st.write("Please [log in](../Login) to access this page.") 

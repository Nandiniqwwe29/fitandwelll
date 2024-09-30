import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="RecoMaster",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background-image: url("https://plus.unsplash.com/premium_photo-1673108852141-e8c3c22a4a22?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-position: center;
        background-size: cover;
        height: 100vh; /* Ensure full viewport height */
        overflow: hidden; /* Hide scrollbar */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Overlay to darken the background for better text visibility */
    .overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: -1;
    }

    /* Main container for centering content */
    .main-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 20px;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
    }

    /* Header styling */
    .header h1 {
        color: #fff900;
        font-size: 4em;
        margin: 0;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }

    .header h2 {
        color: #FFFAFA;
        font-size: 1.5em;
        margin: 10px 0 20px;
        font-family: 'Arial', sans-serif;
    }

    /* Signup button styling */
    .signup-btn {
        background-color: #fff900;
        color: #000; /* Changed to black for better contrast */
        padding: 15px 25px;
        border-radius: 8px;
        text-decoration: none;
        font-size: 1.4em;
        display: inline-block;
        transition: background-color 0.3s ease, transform 0.3s ease;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }

    .signup-btn:hover {
        background-color: #e6c800; /* Slightly darker on hover */
        transform: scale(1.05);
    }

    /* Ensure the main container is above the overlay */
    .main-container {
        position: relative;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content with overlay and centered container
st.markdown(
    """
    <div class="overlay"></div>
    <div class="main-container">
        <div class="header">
            <h1>RecoMaster</h1>
            <h2>Your Ultimate Food Guide</h2>
        </div>
        <a href="http://localhost:8501/Signup" class="signup-btn">Join Us Now</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar content
st.sidebar.success("Select a recommendation app.")

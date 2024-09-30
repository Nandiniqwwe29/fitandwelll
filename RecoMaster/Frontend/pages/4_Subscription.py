import base64
import streamlit as st
import requests

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your local background image
image_path = "C:/RecoMaster/Frontend/Assets/signbg.jpg"  # Ensure this path is correct

# Base64 encode the image
base64_image = get_base64_image(image_path)

# Set the background image and title styles
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
        color: black; /* Title text color */
        text-align: center; /* Center the title */
        font-size: 2.5em; /* Title font size */
        margin-top: 50px; /* Add some space from the top */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Check if the user is logged in
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("You need to log in to subscribe. [Go to Login Page](../Login)")
elif 'id' not in st.session_state:
    st.warning("User ID not found. Please log in again.")
else:
    # Centered title with CSS class
    st.markdown('<h1 class="title">Subscription Plans</h1>', unsafe_allow_html=True)

    subscription_options = {
        "Weekly - ₹99": 99,
        "Monthly - ₹299": 299,
        "Yearly - ₹999": 999
    }

    # Select a plan
    selected_plan = st.radio("Select a Plan:", list(subscription_options.keys()))
    selected_amount = subscription_options[selected_plan]

    st.write(f"You selected: {selected_plan} (₹{selected_amount})")

    # Collect user details
    email = st.text_input("Enter your email")
    contact = st.text_input("Enter your contact number")

    # Proceed with payment
    if st.button("Proceed to Payment"):
        if email and contact:
            # Send the request to FastAPI to create a payment link
            response = requests.post("http://127.0.0.1:8080/create_payment_link/", 
                                         json={"amount": selected_amount, "email": email, "contact": contact})

            # Check if payment link creation is successful
            if response.status_code == 200:
                payment_link = response.json().get("payment_link")
                if payment_link:
                    st.write("Click the link below to make your payment:")
                    st.markdown(f"[Pay Now]({payment_link})", unsafe_allow_html=True)
                else:
                    st.error("Failed to create payment link. Please try again.")
            else:
                st.error("Failed to initiate payment. Please try again.")
        else:
            st.warning("Please enter both email and contact number to proceed.")

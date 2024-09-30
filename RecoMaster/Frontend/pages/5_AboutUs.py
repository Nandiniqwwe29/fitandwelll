import base64
import streamlit as st

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your local background image
image_path = "C:/RecoMaster/Frontend/Assets/signbg.jpg"  # Ensure this path is correct

# Base64 encode the image
base64_image = get_base64_image(image_path)

# Set the background image and text styles
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
    .bold-black {{
        color: black; /* Text color */
        font-weight: bold; /* Bold text */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title and Subtitle
st.markdown('<h1 class="bold-black">About Us</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="bold-black">Empowering Healthy Eating with Personalized Diet Recommendations</h2>', unsafe_allow_html=True)

# Introduction
st.markdown('<p>Welcome to our Diet Recommendation System! Our mission is to make healthy eating simple, personalized, '
            'and accessible. We understand that every individual is unique, and so are their dietary needs. Whether you\'re managing '
            'a health condition like diabetes or simply striving for better nutrition, our platform is here to guide you with tailored meal suggestions.</p>', 
            unsafe_allow_html=True)

# About the Project
st.markdown('<h2 class="bold-black">What We Do</h2>', unsafe_allow_html=True)
st.markdown('<p>We use advanced algorithms to analyze user inputs, including dietary preferences and health conditions, to provide customized meal recommendations. '
            'By offering meals that fit your health needs, we aim to help you achieve your wellness goals efficiently.</p>', 
            unsafe_allow_html=True)

# How It Works
st.markdown('<h2 class="bold-black">How It Works</h2>', unsafe_allow_html=True)
st.markdown('<p class="bold-black">Our recommendation system processes the following:</p>', unsafe_allow_html=True)
st.markdown('''<ul>
    <li>Diet Preferences: Vegetarian, Non-Vegetarian, Vegan</li>
    <li>Health Conditions: Suggests meals optimized for managing specific conditions</li>
    <li>Nutritional Balance: Ensures your meals are balanced with the right nutrients</li>
</ul>
''', unsafe_allow_html=True)
st.markdown('<p>With this information, we generate meal plans that are not only nutritious but also delicious, making it easier to stick to a healthy eating routine.</p>', unsafe_allow_html=True)

# Call to Action
st.markdown('<p class="bold-black"><strong>Ready to Start Your Journey to Healthier Eating?</strong><br>', unsafe_allow_html=True)



# Footer
st.write("---")
st.markdown("<p class='bold-black'><strong>© 2024 Diet Recommendation System</strong></p>", unsafe_allow_html=True)

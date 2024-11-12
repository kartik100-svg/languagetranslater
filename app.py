import streamlit as st
from googletrans import Translator
from languages import *  # Ensure this contains your list of languages

# Set page layout and title
st.set_page_config(layout="centered")

# Define custom styling with HTML and CSS for text, buttons, and output
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Poppins:300,400,600,700&display=swap');

    /* General page setup */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        font-family: 'Poppins', sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    /* Animated box container */
    # .box {
    #     position: relative;
    #     width: 100%;
    #     max-width: 600px;
    #     min-height: 500px;
    #     padding: 4px;
    #     margin: 10px;
    #     display: flex;
    #     flex-direction: column;
    #     align-items: center;
    #     background: #303030;
    #     border-radius: 15px;
    #     box-shadow: 0 0 15px #01dbc2;
    #     overflow: hidden;
    # }

    # /* Rotating border animation */
    # .box::before {
    #     content: '';
    #     position: absolute;
    #     top: -2px;
    #     left: -2px;
    #     right: -2px;
    #     bottom: -2px;
    #     background: conic-gradient(#01dbc2, transparent);
    #     border-radius: 15px;
    #     padding: 4px;
    #     margin: 5px;
    #     animation: rotate 6s linear infinite;
    #     z-index: -1;
    # }

    # @keyframes rotate {
    #     from { transform: rotate(0deg); }
    #     to { transform: rotate(360deg); }
    # }

    /* Title style */
    .title {
        font-size: 28px;
        color: #01dbc2;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* Input and button styling */
    .input-box, .select-box, .button {
        background-color: #292929;
        color: #fff;
        padding: 12px;
        border-radius: 8px;
        border: none;
        width: 100%;
        max-width: 500px;
        margin: 10px 0;
        box-shadow: 0 0 10px #01dbc2;
        font-size: 18px;
    }
    .button {
        background-color: #01dbc2;
        color: #222;
        cursor: pointer;
        transition: background 0.3s ease;
        font-weight: bold;
    }
    .button:hover {
        background-color: #FFB6C1;
    }

    /* Output box style */
    .output-box {
        font-size: 20px;
        color: #4CAF50;
        background-color: #292929;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 0 10px #01dbc2;
        width: 100%;
        max-width: 500px;
        min-height: 100px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Start the main container with animation
st.markdown('<div class="box">', unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">Language Translation App</h1>', unsafe_allow_html=True)

# Input area for text to translate
source_text = st.text_area(
    "Enter text to translate:", 
    placeholder="Type your text here...", 
    height=150,
    help="Enter the text you want to translate."
)

# Select box for target language
selected_language = st.selectbox(
    "Choose Target Language:", 
    languages, 
    index=0,
    help="Select the language you want the text translated to."
)

# Translate button and output
if st.button("Translate", help="Click to translate"):
    if source_text.strip():
        translator = Translator()
        out = translator.translate(source_text, dest=selected_language)
        # Display the translated text in output box
        st.markdown(f'<div class="output-box">{out.text}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to translate!")

# Close the main container
st.markdown('</div>', unsafe_allow_html=True)

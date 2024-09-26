import numpy as np
import pandas as pd
import easyocr
import streamlit as st
from PIL import Image
import cv2
import base64
import pyttsx3  # Text-to-Speech library

# Set the page config with a custom favicon
st.set_page_config(page_title="OCR App", page_icon="generative-image.ico")

# Function to add app background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(f"""<style>.stApp {{background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
    background-size: cover}}</style>""", unsafe_allow_html=True)

def display_ocr_image(img, results):
    img_np = np.array(img)

    for detection in results:
        top_left = tuple([int(val) for val in detection[0][0]])
        bottom_right = tuple([int(val) for val in detection[0][2]])
        text = detection[1]
        font = cv2.FONT_HERSHEY_COMPLEX

        cv2.rectangle(img_np, top_left, bottom_right, (0, 255, 0), 5)
        cv2.putText(img_np, text, top_left, font, 1, (125, 29, 241), 2, cv2.LINE_AA)

    # Display the image with bounding boxes and text
    st.image(img_np, channels="BGR", use_column_width=True)

def extracted_text(col):
    return " , ".join(img_df[col])

# Function for Text-to-Speech (TTS)
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to download extracted text
def download_text(text):
    b64 = base64.b64encode(text.encode()).decode()  # Convert to base64
    href = f'<a href="data:file/txt;base64,{b64}" download="extracted_text.txt">Download Extracted Text</a>'
    st.markdown(href, unsafe_allow_html=True)

# Streamlit app
st.markdown("""
    <svg width="600" height="100">
        <text x="50%" y="50%" font-family="monospace" font-size="42px" fill="Turquoise" text-anchor="middle" stroke="white"
         stroke-width="0.3" stroke-linejoin="round"> 🌐 TextVision OCR 🔍📃
        </text>
    </svg>
""", unsafe_allow_html=True)

add_bg_from_local('pic3.jpg')

# Manually defined list of supported languages
languages_supported = [
    'en',  # English
    'hi',  # Hindi
    'es',  # Spanish
    'fr',  # French
    'de',  # German
    'zh',  # Chinese
    'ja',  # Japanese
    'ar',  # Arabic
    'it',  # Italian
    'pt',  # Portuguese
    # Add more languages as needed
]

# Dropdown to select multiple languages supported by EasyOCR
selected_languages = st.multiselect(
    "Select the language(s) for OCR", options=languages_supported, default=['en']
)

file = st.file_uploader(label="Upload Image Here (png/jpg/jpeg):", type=['png', 'jpg', 'jpeg'])

if file is not None:
    image = Image.open(file)
    st.image(image)

    # Initialize EasyOCR reader with selected languages
    reader = easyocr.Reader(selected_languages, gpu=False)
    results = reader.readtext(np.array(image))

    img_df = pd.DataFrame(results, columns=['bbox', 'Predicted Text', 'Prediction Confidence'])

    # Getting all text extracted
    text_combined = extracted_text(col='Predicted Text')
    st.write("Text Generated :- ", text_combined)

    # Printing results in tabular form
    st.write("Table Showing Predicted Text and Prediction Confidence: ")
    st.table(img_df.iloc[:, 1:])

    # getting final image with drawing annotations
    display_ocr_image(image, results)

    # Text-to-Speech Feature
    if st.button("Play Extracted Text"):
        text_to_speech(text_combined)

    # Download Text as .txt Feature
    download_text(text_combined)

else:
    st.warning("!! Please Upload your image !!")

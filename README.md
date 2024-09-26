# TextVision OCR

TextVision OCR is a powerful Optical Character Recognition (OCR) web application designed to accurately extract text from images in various formats such as PNG, JPG, and JPEG. Utilizing PaddleOCR, the application effectively recognizes text across different languages and presents it in a user-friendly interface. The project not only extracts text but also provides a visual representation of detected text through bounding boxes, allowing users to verify the accuracy of the recognition. Additionally, users can easily download the extracted text as a .txt file for further use.

## Features:

Multi-Language Support: Leverages PaddleOCR's capabilities to recognize text in multiple languages. Users can configure the language parameter to accommodate diverse linguistic needs.

User-Friendly Interface: Built with Streamlit, the application offers a clean and intuitive interface, making it easy for users to upload images and view results without technical hurdles.

Text Extraction with Visual Feedback:As the application processes the uploaded image, it displays the detected text along with bounding boxes around the recognized areas, enhancing user understanding and verification of results.

Confidence Scores: Each extracted text element is accompanied by a confidence score, providing insight into the accuracy of the OCR results and helping users assess the reliability of the extraction.

Downloadable Output: Users can download the extracted text in a .txt format, facilitating easy access and further manipulation of the data for their projects or needs.

## How to run this code:
Step1- Clone the repository to your local machine. <br />
Step2- Install the required dependencies using pip install -r requirements.txt.<br />
Step3- Run the Streamlit app locally using streamlit run app.py.<br />
Step4- Upload an image containing text to perform OCR.<br />
Step5- View the extracted text along with prediction confidence scores in the table.<br />
Step6- Visualize the uploaded image with annotated bounding boxes around detected text.<br />

## Requirements:

Python Version: Python 3.6 or later <br />
### Dependencies:<br />
EasyOCR – For Optical Character Recognition (OCR) functionality.<br />
Streamlit – For building the user interface and app hosting.<br />
OpenCV (cv2) – For image processing and handling.<br />
NumPy – For numerical operations and array handling.<br />
Pandas – For managing tabular data.<br />
Pillow (PIL) – For image manipulation.<br />
Base64 – For handling image encoding for background and file download links.<br />
PyPDF2 – For generating searchable PDFs from extracted text.<br />
ReportLab – For PDF creation and rendering images.<br />

[Live Demo](https://textvision-ocr-fneyfwoquurkxtzvrik2o6.streamlit.app/)

TextVision OCR combines advanced OCR technology with user-centric design to deliver a robust solution for text extraction tasks. Whether for academic purposes, business applications, or personal projects, this tool provides essential features to meet various user needs in a seamless manner.

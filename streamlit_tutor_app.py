import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline
import pytesseract
import time



def main():
    st.header("Phantom Tutor")
    st.markdown(
        """
This demo app is using for LLM-based tutors.
The models sources include HuggingFace and OpenAI.
Supports hard sciences (computer science, analytics, and math). Visuals (graphs, data tables) can be generated with prompts.
There are two windows "summarize" and "explain".
"""
    )
    
    
    computer_science = "Computer Science"
    data_analytics = "Data Analytics"
    math = "Math"
    app_mode = st.selectbox("Choose the app mode", [computer_science, data_analytics, math])

    if app_mode == computer_science :
        model = pipeline('summarization')
    elif app_mode == data_analytics :
        model = pipeline('summarization')   
    elif app_mode == math:
        model = pipeline('summarization')

# Load the OCR model
pytesseract.pytesseract.tesseract_cmd = r"<path-to-tesseract-executable>"
        
# Define a function that takes a picture and returns the OCR output as a string
def ocr(image):
    return pytesseract.image_to_string(image)

def summarize(text):
    summarizer = model
    summarized_text = summarizer(input, min_length = 20,  max_length = 120, do_sample=False)[0]['summary_text']
    return summarized_text
       
main()        
        
article = "Anger and confusion overflowed at the Olympic mixed-team ski jumping final in China after five female competitors were disqualified from the event by officials who said their jumpsuits didn't comply with the rules."
input = st.text_area("Insert Text", article)

# Add a button to the Streamlit app that allows the user to take a picture
st.button("Take a picture")

# When the button is clicked, take a picture and perform OCR and summarization
if st.button:
    picture = st.camera_input("Take a picture")
    if picture:
        image = st.image(picture)
    text = ocr(image)
    summary = summarize(text)
    st.write("OCR Output:", text)
    st.write("Summarized Output:", summary)

# Create an iframe to display a webpage of the user's choice
url = st.text_input("Enter the URL of the webpage you want to display")
components.iframe(url, width=800, height=600)


  



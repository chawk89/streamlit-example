import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline, TrOCRProcessor, VisionEncoderDecoderModel
import pytesseract
import numpy as np
from PIL import Image
from io import BytesIO
import openai




def main():
    st.header("Sherpa Tutor")
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
        pass
        #model = pipeline('summarization')
    elif app_mode == data_analytics :
        pass
        #model = pipeline('summarization')   
    elif app_mode == math:
        pass
        #model = pipeline('summarization')

        
# Define a function that takes a picture and returns the OCR output as a string
def ocr(image):
    # Convert the image to a bytes object
    bytes_data = image.getvalue()
    
    # Open the bytes object as a PIL image
    pil_image = Image.open(BytesIO(bytes_data))
    
    # Perform OCR on the PIL image
    text = pytesseract.image_to_string(pil_image)

    return text    


# Set the OpenAI API key as an environment variable
openai.api_key = st.secrets["api_key"]
# Set the model to use
model_engine = "text-currie"

def summarize_text(text):
  # Use the openai API to summarize the text
  summary = openai.Completion.create(
    engine=model_engine,
    prompt=f"Summarize this text:\n{text}\n",
    max_tokens=200,
    temperature=0.7,
  ).text
  return summary


#def summarize(text):
    #summarizer = model
    #summarized_text = summarizer(input, min_length = 20,  max_length = 120, do_sample=False)[0]['summary_text']
    #return summarized_text
       
main()        
        
# Create the selection box
input_type = st.radio("Input type", ["free text", "image"])
text_input = st.text_input("Enter your text here:")

# If the user selects "image", show a button
if input_type == "image":
    # Add a button to the Streamlit app that allows the user to take a picture
    st.button("Take a picture")

# When the button is clicked, take a picture and perform OCR and summarization
# When the button is clicked, take a picture or upload an image and perform OCR
if st.button:
    image = st.camera_input("Take a picture or upload an image")
    
# Check if the image is None
if image is not None:
    st.image(image, caption="Taken or uploaded image", use_column_width=True)
    text = ocr(image)
    st.write("OCR Output:", text)
else:
    st.write("No image was taken or uploaded")

if text_input:
    summarized_text = summarize_text(text_input)
    st.write(summarized_text)
  



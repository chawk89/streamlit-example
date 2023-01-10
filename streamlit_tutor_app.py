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
There are two windows "task" and "chat".
"""
    )

main()  
    
summarize = "Summarize"
make_interesting = "Make it interesting!"
help_solve = "Help me solve!"
app_mode = st.selectbox("Choose the app mode", [summarize, make_interesting, help_solve])

if app_mode == summarize :
    prompt = "Summarize this text as if I'm a 2nd grader:"
    model = "text-curie-001"
elif app_mode == make_interesting :
    prompt = "Make the following a lot more interesting:"
    model = "text-curie-001"  
elif app_mode == help_solve:
    prompt = "Help me solve the following step by step:" 
    model = "text-davinci-003" 
    
    

        
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

def process_text(text):
  # Use the openai API to summarize the text
  response = openai.Completion.create(
    model = model,
    prompt= prompt + f"\n{text}\n",
    max_tokens=300,
    temperature=0.7,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  st.write(prompt + "\n(text)\n")  
  return response


#def summarize(text):
    #summarizer = model
    #summarized_text = summarizer(input, min_length = 20,  max_length = 120, do_sample=False)[0]['summary_text']
    #return summarized_text
       
      
        
# Create the selection box
input_type = st.radio("Input type", ["free text", "image"])
text_input = st.text_input("Enter your text here:")

# If the user selects "image", show a button
if input_type == "image":
    # Add a button to the Streamlit app that allows the user to take a picture
    st.button("Take a picture")
# When the button is clicked, take a picture or upload an image and perform OCR
if st.button:
    image = st.camera_input("Take a picture or upload an image")
    
# Check if the image is None
if image is not None:
    st.image(image, caption="Taken or uploaded image", use_column_width=True)
    text_input = ocr(image)
    st.write("OCR Output:", text)
else:
    text_input = text_input

if text_input:
    summarization = process_text(text_input)
    st.write(summarization.choices[0]['text'])
    st.write(summarization)
  



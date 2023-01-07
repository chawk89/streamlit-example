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

#def summarize(text):
    #summarizer = model
    #summarized_text = summarizer(input, min_length = 20,  max_length = 120, do_sample=False)[0]['summary_text']
    #return summarized_text
       
main()        
        

# Add a button to the Streamlit app that allows the user to take a picture
st.button("Take a picture")

# When the button is clicked, take a picture and perform OCR and summarization
# When the button is clicked, take a picture or upload an image and perform OCR
if st.button:
    image = st.camera_input("Take a picture or upload an image")
    
        # Convert the image to a numpy array
    image_array = np.array(image)

    # Convert the numpy array to a PIL image
    pil_image = Image.fromarray(image_array)
    
    st.image(pil_image, caption="Taken or uploaded image", use_column_width=True)
    text = ocr(image)
    st.write("OCR Output:", text)


  



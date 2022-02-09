import streamlit as st
from transformers import pipeline
import time

"""
# Text Summarizer

Add a snippet of an article to summarize. It may take 5-10 seconds to complete the task! The text summarizer is a transformer model from huggingface.co, pretrained on publisher content. 
"""

article = "Anger and confusion overflowed at the Olympic mixed-team ski jumping final in China after five female competitors were disqualified from the event by officials who said their jumpsuits didn't comply with the rules."
input = st.text_area("Insert Text", article)
st.write('Character count: ', len(input))

if len(input) > 1500:
    st.write("Input may be just a bit too long!")


with st.spinner('Wait for it...'):
    summarizer = pipeline('summarization')
    output = summarizer(input, min_length = 20,  max_length = 120, do_sample=False)[0]['summary_text']
st.success('Done!')
    

st.header('Summary:')
st.subheader(output)
st.balloons()

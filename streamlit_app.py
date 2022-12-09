import streamlit as st
from transformers import pipeline
import pandas as pd
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
        app_sst(
            str(MODEL_LOCAL_PATH), str(LANG_MODEL_LOCAL_PATH), lm_alpha, lm_beta, beam
        )
    elif app_mode == data_analytics :
        app_sst(
            str(MODEL_LOCAL_PATH), str(LANG_MODEL_LOCAL_PATH), lm_alpha, lm_beta, beam
        )    
    elif app_mode == math:
        app_sst_with_video(
            str(MODEL_LOCAL_PATH), str(LANG_MODEL_LOCAL_PATH), lm_alpha, lm_beta, beam
        )


article = "Anger and confusion overflowed at the Olympic mixed-team ski jumping final in China after five female competitors were disqualified from the event by officials who said their jumpsuits didn't comply with the rules."
input = st.text_area("Insert Text", article)


with st.spinner('Wait for it...'):
    summarizer = pipeline('summarization')
    output = summarizer(input, min_length = 20,  max_length = 120, do_sample=False)[0]['summary_text']
    
st.success('Done!')

input = st.text_area("Talk to me,baby!", chat)

######

choice = st.sidebar.radio("Pick an Olympic medal data set",["bronze","siver","gold"])

st.sidebar.image("https://sportshub.cbsistatic.com/i/r/2021/12/06/e072d88c-0cd9-4390-b919-353d85710ebb/thumbnail/770x433/94d78d1afd5713db52124e1317f4e8cb/beijing-2022.jpg")    
st.sidebar.video("https://www.youtube.com/watch?v=SPKckEXhWwU")

word_count = len(input.split())

st.write('Character count: ', len(input))
st.write('Word count: ', word_count)
"Please allow a few seconds for me to digest! Any radio button selection may add to the time."

if len(input) > 2000:
    st.write("Input may be just a bit too long!")



gold = pd.DataFrame({ 'Year': ['2006','2010','2014','2018'],
                    'Medals': [9,9,9,9]
                       })

silver = pd.DataFrame({ 'Year':['2006','2010','2014','2018'],
                    'Medals': [9,15,9,8]
                       })

bronze = pd.DataFrame({ 'Year': ['2006','2010','2014','2018'],
                    'Medals': [7,13,10,6]
                       })


if choice == "gold":
    st.sidebar.dataframe(gold)
    st.sidebar.table(gold)
    st.sidebar.line_chart(gold.rename(columns={'Year':'index'}).set_index('index'))
    st.sidebar.bar_chart(gold.rename(columns={'Year':'index'}).set_index('index'))
elif choice == "silver":
    st.sidebar.dataframe(silver)
    st.sidebar.table(silver)
    st.sidebar.line_chart(silver.rename(columns={'Year':'index'}).set_index('index'))
    st.sidebar.bar_chart(siver.rename(columns={'Year':'index'}).set_index('index'))
else:
    st.sidebar.dataframe(bronze)
    st.sidebar.table(bronze)
    st.sidebar.line_chart(bronze.rename(columns={'Year':'index'}).set_index('index'))
    st.sidebar.bar_chart(bronze.rename(columns={'Year':'index'}).set_index('index'))




    
c = st.empty()
c.header('Summary:')
st.subheader(output)
st.balloons()

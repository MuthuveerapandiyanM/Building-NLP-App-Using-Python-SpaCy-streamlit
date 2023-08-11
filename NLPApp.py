#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st 
from time import sleep
from stqdm import stqdm # for getting animation after submit event 
import pandas as pd
from transformers import pipeline
import json
import spacy
import spacy_streamlit

def draw_all(key, plot=False):
    st.write(
        """
        # Natural language processing (NLP) Web App : Unleash the Magic of Text
        This is a Natural Language Processing Based Web App that can do anything 
        u can imagine with the Text.
        Natural Language Processing (NLP) is a computational technique to understand 
        the human language in the way they spoke and write.
        NLP is a sub field of Artificial Intelligence (AI) to understand the context 
        of text just like humans.
        

        
        ```python
        # Behold the Key Features of this Enchanted App:
        Advanced Text Summarization 📚
        Captivating Named Entity Recognition 🎭
        Sentiment Analysis: Exploring Emotional Landscapes 🌄
        Text Completion: Crafting Textual Gems 💎
       
        ```
        """
    )
with st.sidebar:
    draw_all("Scroll Panel")
    
def main():
    st.title("Natural language processing (NLP) Web App")
    menu= ["--SELECT--", "Text Summarizer", "Named Entity Recognizer", "Sentiment Analysis",'Text Completion']
    choice = st.sidebar.selectbox("Choose What You Wanna to Explore !!", menu)
    if choice=="--SELECT--":
        
        st.header("Welcome to a Natural Language Processing (NLP) marvel! 🚀 😱")
        
        st.write("""Discover the NLP Web App, a captivating platform powered by pretrained transformers. 
                    From advanced text summarization to sentiment analysis, this tool lets you unravel the magic 
                    within textual data with ease.
                    This App is built using pretrained transformers which are capable of doing wonders with 
                    the Textual data.
                 """)
        st.image("C:/Users/ELCOT/Desktop/New folder/nlp_todays_news.png")
        
    elif choice=="Text Summarizer":  
        st.subheader("Summarization")
        st.write("Enter Your Text to Summarize")
        raw_text = st.text_area('Your Text','Enter Your Text Here')
        num_words = st.number_input("Enter Number of Words in Summary")
            
        if raw_text!='' and num_words is not None:        
            num_words = int(num_words)
            summarizer = pipeline('summarization')
            summary = summarizer(raw_text, min_length=num_words, max_length=50)
            s1 = json.dumps(summary[0])
            d2 =json.loads(s1)
            result_summary = d2['summary_test']
            result_summary = '. '.join(list(map(lambda x: x.strip().capitalize(),
                                           result_summary.split('.'))))
            st.write(f"Here's your Summary : {result_summary}")
            
    elif choice=="Named Entity Recognizer":
        nlp = spacy.load("en_core_web_trf")
        st.subheader("Captivating Named Entity Recognition 🎭")
        st.write("Enter the Text Here !")
        raw_entity = st.text_area("Your Text",'Enter Text Here')
        if raw_entity !='Enter Text Here':
            doc = nlp(raw_entity)
            for _ in stqdm(range(50), desc="Feel free to take the time you need to find the optimal words for your beautiful sentence."):
                sleep(0.1)
            spacy_stramlit.visualize_ner(doc, labels=nlp.get_pipe('ner').labels, title='List of Entities')
            
    elif choice=="Sentiment Analysis":
        st.subheader('Sentiment Analysis: Exploring Emotional Landscapes 🌄')
        sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased")
        st.write("Enter the Text To Explore its Sentiment")
        
        raw_sentiment = st.text_area("Your Text","Enter Text")
        if raw_sentiment !='Enter Text Here':
            result = sentiment_analysis(raw_sentiment)[0]
            sentiment = result['label']
            for _ in stqdm(range(50), desc= "Please wait a bit. Result is processing"):
                sleep(0.1)
            if sentiment == 'POSITIVE':
                st.write("""# This Text has a Positive Sentiment.  🤗""")
            elif sentiment == 'NEGATIVE':
                st.write("""# This Text has a Negative Sentiment.  😤""")
            elif sentiment == 'NEUTRAL':
                st.write("""# This Text has a Negative Sentiment.  😐""")  
                
    elif choice=="Text Completion":
        st.subheader("Text Completion: Crafting Textual Gems 💎")
        st.write("Enter the uncomplete Text to complete")
        text_generation = pipeline("text-generation")
        message = st.text_area("Your Text",'Enter Text wanna to complete')
        
        if message !='Enter Text to complete':
            generator = text_generator(message)
            s1 = json.dumps(generator[0])
            d2 = json.loads(s1)
            generated_text = d2['generated_text']
            generated_text = '. '.join(list(map(lambda x: x.strip().capitalize(), generated_text.split('.'))))
            st.write(f" Here your Complete piece of Text:\n {generated_text}")

if __name__ == '__main__':
     main()
    


# In[ ]:





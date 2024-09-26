import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# STEPS:
# 1. Create the Virtual Environment           virtualenv.venv
# 2. Activate the Virtual Env. (ie: .venv)    source .venv/Scripts/activate 
# 3. Write, Save and Run the python code

# For API key to be kept secretive, we are saving it in local environment
from dotenv import load_dotenv                # Import Local Environment
import os 
load_dotenv()                                 # Connecting GitHub to GoogleAI
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# Linking Google Api to Steamlit 
# Providing authorization to Streamlit application to access the Google-Api-Key
headers = {'authorization': st.secrets["GOOGLE-API-KEY"], "content-type": "application/json"}

# Design the Web Page
st.title('Movie Recommender System')
user_input = st.text_input('Enter the Movie Title, Genre, or Keyword')

# streamlit run app.py - to run the code and opening the application 

demo_template = '''Based on {user_input} provide Movie Recommendations'''
template = PromptTemplate(input_variables = ['user_input'],
                          template = demo_template)

# Google GeminiAI Model
llm = ChatGoogleGenerativeAI(model = 'gemini-pro', api_key = 'GOOGLE-API-KEY')

if user_input:
    prompt = template.format(user_input = user_input)
    recommendations = llm.predict(text = prompt)
    st.write(f"Recommendations for you: \n {recommendations}")
else:
    st.write(' ')
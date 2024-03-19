import google.generativeai as genai
import streamlit as st

def load_model():

    genai.configure(api_key = st.secrets['gAIzaSyDeSVye3GKNm_JlblddR1GzTG5lczNvD8o'])

    return genai.GenerativeModel("gemini-pro")


def get_output(question):
    model = load_model()
    response = model.generate_content(contents=question)
    return response.text

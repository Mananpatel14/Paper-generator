import openai
import streamlit as st

# Load the OpenAI Generative Model
def load_model():
    openai.api_key = st.secrets["openai"]["api_key"]
    return openai.ChatCompletion.create(model="gpt-3.5-turbo")

# Load the model when the application starts
model = load_model()

# Function to generate content based on a question
def get_output(question):
    response = model.create(
        prompt=question,
        max_tokens=150,
        temperature=0.7,
        stop=['\n']
    )
    return response.choices[0].text.strip()

# Streamlit app code
st.title("Generative AI Example")

question = st.text_input("Enter your question:")
if st.button("Generate Response"):
    if question:
        output = get_output(question)
        st.text_area("Generated Response:", value=output, height=150)
    else:
        st.warning("Please enter a question.")





'''import google.generativeai as genai
import streamlit as st

def load_model():

    genai.configure(api_key = st.secrets['google_cloud_api_key'])

    return genai.GenerativeModel("gemini-pro")


def get_output(question):
    model = load_model()
    response = model.generate_content(contents=question)
    return response.text'''

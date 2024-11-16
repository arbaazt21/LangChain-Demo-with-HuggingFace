import os
from constants import hf_api_key  # Ensure this contains your Hugging Face API token

# Set Hugging Face API Token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api_key

from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st

# Define the Hugging Face model endpoint
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

# Pass temperature directly as a parameter instead of inside `model_kwargs`
llm = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.7)

# Set up Streamlit app
st.title("Langchain DEMO with HuggingFace")
input_text = st.text_input("Enter the topic you want to search:")

if input_text:
    st.write(llm(input_text))
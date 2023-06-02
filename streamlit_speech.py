import streamlit as st
from transformers import pipeline

p = pipeline("automatic-speech-recognition")

st.title("Speech-To-Text!")

audio_file = st.file_uploader("Upload Audio", type=["wav","mp3","m4a"])

@st.cache

# def load_speech_model():

import streamlit as st
from transformers import pipeline

p = pipeline("automatic-speech-recognition")

st.title("Speech-To-Text!")

audio_file = st.file_uploader("Upload Audio", type=["wav","mp3","m4a"])

@st.cache

def transcribe(audio, state=""):
    # time.sleep(3)
    text = p(audio)["text"]
    state += text + " "
    return state, state

if st.sidebar.button("Load audio"):
    state = transcribe()

if st.sidebar("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Generating Audio")
        audio_bytes = audio_file.read()
        audio = state
        st.audio(audio)

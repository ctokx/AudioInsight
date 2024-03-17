import tempfile
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)

def summarize_with_gpt3(transcribed_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize this text: {transcribed_text}"}
        ]
    )
    
    summary_text = response.choices[0].message.content
    return summary_text

def transcribe_and_summarize(uploaded_file):

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        audio_file_path = tmp_file.name

    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )

    transcribed_text = transcription.text

    summary_text = summarize_with_gpt3(transcribed_text)

    language_detected = "en"
    
    return language_detected, transcribed_text, summary_text


st.title("Audio Transcription and Summarization App")

audio_file = st.file_uploader("Upload an audio file", type=['wav', 'mp3', 'ogg'])

if audio_file is not None:
    with st.spinner('Transcribing and summarizing...'):
        language_detected, transcribed_text, summary_text = transcribe_and_summarize(audio_file)
        
    st.write(f"Detected Language: {language_detected}")
    st.text_area("Transcribed Text", value=transcribed_text, height=300)
    st.text_area("Summary", value=summary_text, height=150)

import tempfile
import streamlit as st
import whisper
from transformers import pipeline

def transcribe_and_summarize(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        audio_file_path = tmp_file.name


    model = whisper.load_model("base")
    
  
    audio = whisper.load_audio(audio_file_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    

    _, probs = model.detect_language(mel)
    language_detected = max(probs, key=probs.get)
    

    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)
    transcribed_text = result.text
    

    summarizer = pipeline("summarization")
    summary = summarizer(transcribed_text, max_length=700, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text']
    
    return language_detected, transcribed_text, summary_text

# Streamlit UI
st.title("Audio Transcription and Summarization App")

audio_file = st.file_uploader("Upload an audio file", type=['wav', 'mp3', 'ogg'])

if audio_file is not None:
    with st.spinner('Transcribing and summarizing...'):
        language_detected, transcribed_text, summary_text = transcribe_and_summarize(audio_file)
        
    st.write(f"Detected Language: {language_detected}")
    st.text_area("Transcribed Text", value=transcribed_text, height=300)
    st.text_area("Summary", value=summary_text, height=150)

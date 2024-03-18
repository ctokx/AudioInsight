import tempfile
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import OpenAI as LLamaopenai
from llama_index.llms import ChatMessage, MessageRole
from llama_index import ChatPromptTemplate
from llama_index import StorageContext, load_index_from_storage 
from llama_index.evaluation import FaithfulnessEvaluator
from typing import Any
load_dotenv()
INPUT_DIR = 'data/input'
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_contextual_response(query: str) -> Any:
    persist_dir = '/mytmp/index_storage/input_context'

    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    llm = LLamaopenai(model="gpt-3.5-turbo", temperature=0.1, api_key=OPENAI_API_KEY)
    service_context = ServiceContext.from_defaults(llm=llm)


    documents = SimpleDirectoryReader(INPUT_DIR).load_data()
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)


    chat_text_qa_msgs = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content="Summarize the text cover the main aspecs as deatiled as possible. give it in bullet points"
        ),
 
    ]

    text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)
    query_engine = index.as_query_engine()
    formatted_query = text_qa_template.format(query_str=query)

    response = query_engine.query(formatted_query)

    evaluator = FaithfulnessEvaluator(service_context=service_context)
    eval_result = evaluator.evaluate_response(response=response)

    if isinstance(response, str):
        return response
    elif hasattr(response, 'text'):
        return response.text
    elif isinstance(response, list):
        return ' '.join([item.text if hasattr(item, 'text') else str(item) for item in response])
    else:
        return str(response)

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

    transcript_file_path = 'data/input/input.txt'

    os.makedirs(os.path.dirname(transcript_file_path), exist_ok=True)


    with open(transcript_file_path, 'w') as file:
        file.write(transcribed_text)

    summary_text = get_contextual_response("summarize the text")

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

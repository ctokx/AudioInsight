# Simple Audio Transcription and Summarization App

This application is designed to transcribe and summarize audio files using Whisper and Hugging Face's transformers. It's built with Streamlit, making it easy to deploy as a web app. Here's how it works and how you can set it up.

## Features

- **Audio Transcription**: Converts speech in audio files to text.
- **Language Detection**: Automatically detects the language of the audio file.
- **Summarization**: Provides a concise summary of the transcribed text.
- **Streamlit Integration**: Easy-to-use web interface for uploading audio files and viewing results.

## How It Works

The `transcribe_and_summarize` function performs the core operations:

1. **Audio File Processing**: Temporarily saves the uploaded audio file for processing.
2. **Whisper Model Loading**: Uses OpenAI's Whisper model for transcription and language detection.
3. **Audio Preprocessing**: Converts the audio to a format suitable for the Whisper model.
4. **Language Detection**: Determines the most probable language of the audio content.
5. **Transcription**: Transcribes the audio file to text.
6. **Summarization**: Uses a Hugging Face summarization pipeline to create a summary of the transcribed text.
7. **Streamlit UI**: Provides an interface for uploading audio files and displays the detected language, transcribed text, and summary.

## Installation

To run this application, you need Python installed on your machine along with several libraries and tools. Follow these steps to set up the environment:

### Prerequisites

- Python 3.8 or newer
- pip (Python package installer)
- ffmpeg (for audio file processing)

### Library Installations

Install the required Python libraries using pip:

```shell
pip install streamlit
pip install -U openai-whisper
pip install git+https://github.com/openai/whisper.git
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

### FFmpeg Installation

FFmpeg is required for audio processing. Install it according to your operating system:

## Ubuntu or Debian

```shell
sudo apt update && sudo apt install ffmpeg
```

## Windows (using Chocolatey)
```shell
choco install ffmpeg
```
### Usage
- Open the Streamlit app in your web browser.
- Upload an audio file in WAV, MP3, or OGG format.
- Wait for the app to transcribe and summarize the audio file.
- View the detected language, transcribed text, and summary in the app interface.
- Enjoy your streamlined audio processing experience!

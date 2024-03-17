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
```
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

# Audio Transcription and Summarization Comparison

This document outlines the main differences between two approaches for audio transcription and summarization implemented in `local.py` and `api.py`. Each script offers a unique method for processing audio files, with distinct advantages and considerations.

## Overview

- **local.py**: Utilizes local libraries and models for both transcription and summarization tasks. Specifically, it employs the Whisper model for transcription and the Transformers library for summarization.
- **api.py**: Leverages OpenAI's API for both transcription (using Whisper) and summarization (using GPT-3.5), interacting directly with OpenAI's cloud services.

## Technical Differences

### Transcription

- **local.py**: The transcription is performed using a local implementation of the Whisper model. This approach does not require internet connectivity and avoids API usage costs but might be limited by the computational resources of the local machine.
  
- **api.py**: Transcription is handled through OpenAI's API, using the Whisper model. This method benefits from potentially more updated models and offloads computational requirements to OpenAI's servers, at the cost of API usage fees and the need for internet connectivity.

### Summarization

- **local.py**: Summarization is conducted using the Transformers library, typically with models like BART or T5. While effective, the quality and capabilities of the summarization depend on the specific pre-trained model used and its alignment with the content being summarized.
  
- **api.py**: Utilizes OpenAI's GPT-3.5 model via the API for summarization, providing access to one of the most advanced language models available. This can result in more coherent, contextually relevant summaries, especially for complex or nuanced content.

## When to Use Each

### Use `local.py` when:

- Working offline or in environments with restricted internet access.
- Minimizing operational costs is a priority, and you wish to avoid API usage fees.
- Data privacy or security concerns prohibit sending content to external servers for processing.
- The content to be summarized is well-structured and does not require deep contextual understanding for accurate summarization.

### Use `api.py` when:

- The highest quality transcription and summarization are required, leveraging the latest advancements in AI models.
- Internet connectivity is consistent, and the operational budget can accommodate API usage costs.
- You are processing complex, nuanced content that benefits from the advanced understanding capabilities of GPT-3.5.
- Computational resources are limited locally, and offloading processing to the cloud is advantageous.

## Success and Limitations

- **local.py** might struggle with accurately summarizing very long audio files or content with complex nuances, as the summarization models available locally may not always be on par with the latest AI models like GPT-3.5.
  
- **api.py** is generally more successful at producing high-quality summaries for a wide range of contents, including lengthy and nuanced discussions. However, this success comes with the trade-offs of API costs and the requirement for internet connectivity.

In summary, the choice between `local.py` and `api.py` should be guided by the specific requirements of your project, including considerations around internet access, computational resources, operational costs, and the complexity of the content being processed.


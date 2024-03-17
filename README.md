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

| Feature               | local.py                                      | api.py                                        |
|-----------------------|-----------------------------------------------|-----------------------------------------------|
| **Transcription**     | Uses a local implementation of the Whisper model. Does not require internet connectivity. May be limited by the computational resources of the local machine. | Transcription through OpenAI's API, using the Whisper model. Benefits from updated models and offloads computational load to OpenAI's servers. Requires internet connectivity. |
| **Summarization**     | Summarization with the Transformers library, typically with models like BART or T5. Quality depends on the specific pre-trained model used. | Summarization utilizes OpenAI's GPT-3.5 model via the API, providing access to advanced language models for coherent, contextually relevant summaries. |
| **Internet Connectivity** | Not required.                                  | Required for API access.                       |
| **Operational Costs** | Minimized, as it avoids API usage fees.       | Potentially higher due to API usage fees.     |
| **Computational Resources** | Requires significant computational resources for optimal performance, especially for processing large audio files. | Computational load is offloaded to OpenAI's servers. Local resources are less of a concern. |
| **Data Privacy**      | Data is processed locally, offering potentially higher privacy and security. | Data is sent to and processed by external servers, which may raise privacy concerns. |
| **Flexibility**       | No flexibility in changing models or utilizing advanced language models for summarization. | Flexibility to change models (e.g., upgrading to GPT-4 for extremely valuable summaries) is available. However, check the costs on the OpenAI website before proceeding. |

## When to Use Each

### Use `local.py` when:
- You need to work offline or in environments with restricted internet access.
- Minimizing operational costs is a priority, avoiding API usage fees.
- Data privacy or security concerns prohibit sending content to external servers for processing.
- The content to be summarized is well-structured and does not require deep contextual understanding for accurate summarization.
- You have access to very good computational resources, especially important for processing long audio files or ensuring timely processing.

### Use `api.py` when:
- The highest quality transcription and summarization are required, leveraging the latest advancements in AI models.
- Consistent internet connectivity is available, and the operational budget can accommodate API usage costs.
- You are processing complex, nuanced content that benefits from the advanced understanding capabilities of GPT-3.5.
- Limited local computational resources make cloud processing a more viable option.

## Success and Limitations

- **local.py** might struggle with accurately summarizing very long audio files or content with complex nuances, as the summarization models available locally may not always be on par with the latest AI models like GPT-3.5. The requirement for significant computational resources can be a limiting factor for some users.

- **api.py** is generally more successful at producing high-quality summaries for a wide range of contents, including lengthy and nuanced discussions. This success, however, comes with the trade-offs of API costs and the requirement for internet connectivity.

In summary, the choice between `local.py` and `api.py` should be guided by the specific requirements of your project, including considerations around internet access, computational resources, operational costs, and the complexity of the content being processed.
## Running the Application

To run your chosen script, use the command: streamlit run your_preference.py.

If you decide to run the API version, go to the environment variables and set your OpenAI API key.

![Example(?)](https://github.com/ctokx/transcribeandsummarize/blob/main/example.png?raw=true "Elon Musk")

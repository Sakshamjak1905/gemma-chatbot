# Gemma Chatbot

A simple chatbot that runs fully on your own computer. It uses the **gemma2:2b** model through **Ollama**, with a chat interface built in **Streamlit**. No internet or API key is needed once the model is downloaded.

## Features

- Chat with a local AI model
- Remembers the conversation during the session
- Simple web interface in the browser
- Runs offline

## Requirements

- Python 3.9 or newer
- [Ollama](https://ollama.com) installed
- About 2 GB of free disk space for the model

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/Sakshamjak1905/gemma-chatbot.git
   cd gemma-chatbot
   ```

2. Download the model:
   ```
   ollama pull gemma2:2b
   ```

3. Create and activate a virtual environment (Windows):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install the libraries:
   ```
   pip install -r requirements.txt
   ```

## Run

Make sure Ollama is running, then start the app:

```
streamlit run app.py
```

Your browser will open at `http://localhost:8501`.

## Project Structure

```
gemma-chatbot/
├── app.py             # Streamlit chatbot interface
├── test.py            # Quick test that

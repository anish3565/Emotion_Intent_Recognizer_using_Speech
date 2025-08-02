# 🎙️ Real-Time Emotion + Intent Recognizer using Speech

This project provides a real-time pipeline to **transcribe**, **translate**, and **analyze speech** for both **emotions** and **intents** across multiple languages. It supports recording or uploading audio and generates an audible response along with prediction logs.

## 🚀 Features

- 🔍 **Speech Recognition**: Uses OpenAI Whisper for accurate transcription of multilingual audio.
- 🌐 **Language Detection & Translation**: Detects spoken language and translates transcriptions into English.
- 😀 **Emotion Detection**: Classifies emotions such as `Happy`, `Sad`, `Angry`, `Fear`, `Neutral`, etc.
- 🧠 **Intent Recognition**: Identifies the underlying intent using a zero-shot BART model (e.g., `question`, `greeting`, `translate`, etc.).
- 🔊 **Text-to-Speech (TTS)**: Responds with a synthesized voice summary using `pyttsx3`.
- 📝 **Prediction Logging**: Saves all inference results with timestamp and metadata for traceability.

---

## 🖼️ App Interface

The interface supports:

- 🎧 Upload or record audio
- 📄 View original and translated transcriptions
- 😊 See emotion and intent predictions
- 🔁 Listen to AI-generated response

---

## 🛠️ File Structure

```

├── .gitignore               # .gitignore file
├── .python-version          # Python version lock to 3.10.11
├── app.py                   # Gradio UI + main orchestrator
├── emotion_model.py        # Emotion classification model
├── intent_model.py         # BART-based intent classifier
├── logger.py               # JSON/CSV logging for predictions
├── translator.py           # Language detection and translation
├── tts_response.py         # TTS audio generation
├── whisper_transcriber.py  # Whisper-based audio transcription
├── requirements.txt
└── README.md

````

---

## 📦 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
````

Ensure your system supports:

* `torch` with compatible CUDA/CPU
* `transformers`, `whisper`, `pyttsx3`, `gradio`, etc.

---

## ▶️ Run the Application

```bash
python app.py
```

Gradio UI will open in your browser. Use the `--share` flag to make it public.

---

## 📂 Logs

All predictions are logged via `logger.py` to a file (`predictions_log.json` or `.csv`) with:

* Timestamp
* Language
* Original Text
* Translated Text
* Predicted Emotion
* Predicted Intent

---

## 📬 Contact & Author

**Anish Tripathi**
🔹 AI/ML Developer | LLM Engineering | Semantic Search | Vector DBs | RAG Workflows
🔗 [GitHub](https://github.com/anish3565)
📧 [tripathianish12@gmail.com](mailto:tripathianish12@gmail.com)

---
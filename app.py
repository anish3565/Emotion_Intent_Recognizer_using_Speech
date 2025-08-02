import os
import gradio as gr
from whisper_transcriber import transcribe_audio
from translator import translate_to_english
from emotion_model import predict_emotion
from intent_model import predict_intent
from tts_response import generate_tts
from logger import log_prediction

def analyze(audio):
    try:
        if not audio:
            return "No audio received", "", "", "", "", None

        audio_path = audio if isinstance(audio, str) else audio.name
        if not os.path.exists(audio_path):
            return "Audio file not found", "", "", "", "", None

        # 1. Transcribe and detect language
        text, lang = transcribe_audio(audio_path)
        if not text:
            return "Transcription failed", lang, "", "", "", None

        # 2. Translate to English
        translated_text = translate_to_english(text, lang) or "Translation failed"

        # 3. Predict emotion from raw audio
        emotion = predict_emotion(audio_path) or "Unknown"

        # 4. Predict intent from translated text
        intent = predict_intent(translated_text) or "Unknown"

        # 5. Log all values
        log_prediction(lang, text, translated_text, emotion, intent)

        # 6. Generate TTS response
        response_text = f"Detected emotion: {emotion}. Intent: {intent}."
        tts_path = generate_tts(response_text)

        return text, lang, translated_text, emotion, intent, tts_path

    except Exception as e:
        return f"Error: {str(e)}", "", "", "", "", None

# Gradio UI setup
iface = gr.Interface(
    fn=analyze,
    inputs=gr.Audio(type="filepath", label="Upload or Record Audio"),
    outputs=[
        gr.Text(label="Original Transcription"),
        gr.Text(label="Detected Language"),
        gr.Text(label="Translated Text (English)"),
        gr.Text(label="Detected Emotion"),
        gr.Text(label="Predicted Intent"),
        gr.Audio(label="Response Audio")
    ],
    title="🎙️ Real-Time Multilingual Speech Emotion + Intent Recognizer",
    description="Upload or record speech to detect emotion and intent. Supports multilingual input. Powered by Whisper, TTS, Emotion & Intent models."
)

if __name__ == "__main__":
    iface.launch(share=True)
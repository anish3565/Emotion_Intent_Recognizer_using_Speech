import gradio as gr
from whisper_transcriber import transcribe_audio
from translator import translate_to_english
from emotion_model import predict_emotion
from intent_model import predict_intent
from tts_response import generate_tts
from logger import log_prediction

def analyze(audio):
    audio_path = audio if isinstance(audio, str) else audio.name

    # Transcribe and detect language
    text, lang = transcribe_audio(audio_path)

    # Translate to English
    translated_text = translate_to_english(text, lang)

    # Predict emotion and intent
    emotion = predict_emotion(audio_path)
    intent = predict_intent(translated_text)

    # Logging the prediction
    log_prediction(lang, text, translated_text, emotion, intent)

    # TTS response
    tts_path = generate_tts(f"Detected emotion: {emotion}. Intent: {intent}.")

    return text, lang, translated_text, emotion, intent, tts_path

iface = gr.Interface(
    fn=analyze,
    inputs=gr.Audio(type="filepath"),
    outputs=[
        gr.Text(label="Original Transcription"),
        gr.Text(label="Detected Language"),
        gr.Text(label="Translated Text (English)"),
        gr.Text(label="Detected Emotion"),
        gr.Text(label="Predicted Intent"),
        gr.Audio(label="Response Audio")
    ],
    title="🎙️ Speech Emotion + Intent Recognizer",
    description="Record or upload speech to detect emotion and intent in real time"
)

if __name__ == "__main__":
    iface.launch(share=True)
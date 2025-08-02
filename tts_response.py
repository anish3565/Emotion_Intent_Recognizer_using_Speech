import os
from TTS.api import TTS

# Creating the audio output folder
AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Initialize the TTS model
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

def generate_tts(text, filename="response.wav"):
    output_path = os.path.join(AUDIO_DIR, filename)
    tts_model.tts_to_file(text=text, file_path=output_path)
    return output_path
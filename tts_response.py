import pyttsx3
import uuid
import os

def generate_tts(text, out_dir="responses"):
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}.mp3"
    path = os.path.join(out_dir, filename)

    engine = pyttsx3.init()
    engine.save_to_file(text, path)
    engine.runAndWait()

    return path
import random

def predict_emotion(audio_path):
    emotions = ['Happy', 'Sad', 'Angry', 'Fear', 'Surprise', 'Neutral']
    return random.choice(emotions)
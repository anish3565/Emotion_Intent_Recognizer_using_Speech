import csv
import os
from datetime import datetime

def log_prediction(lang, original_text, translated_text, emotion, intent):
    os.makedirs("logs", exist_ok=True)
    file_path = "logs/predictions.csv"
    exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not exists:
            writer.writerow(["Timestamp", "Language", "Original", "Translated", "Emotion", "Intent"])
        writer.writerow([datetime.now(), lang, original_text, translated_text, emotion, intent])
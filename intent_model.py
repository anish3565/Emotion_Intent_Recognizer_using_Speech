from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
labels = ["question", "command", "greeting", "complaint", "feedback", "help"]

def predict_intent(text):
    result = classifier(text, labels)
    return result['labels'][0]
from deep_translator import GoogleTranslator

def translate_to_english(text, src_lang):
    if src_lang == 'en':
        return text
    try:
        return GoogleTranslator(source=src_lang, target='en').translate(text)
    except:
        return text
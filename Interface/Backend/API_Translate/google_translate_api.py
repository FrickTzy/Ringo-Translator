from .translator_method_interface import TranslatorMethod


class GoogleTranslateAPI(TranslatorMethod):
    def __init__(self):
        pass

    def detect_language(text):
        translator = Translator()
        detected = translator.detect(text)
        return detected.lang

    def translate(text, dest_language):
        translator = Translator()
        translated = translator.translate(text, dest=dest_language)
        return translated.text
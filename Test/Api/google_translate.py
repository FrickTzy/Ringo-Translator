from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.co.kr'])


def detect_language(text):
    detected = translator.detect(text)
    return detected.lang


def translate_text(text, source_language, dest_language):
    translated = translator.translate(text=text, src=source_language, dest=dest_language)
    return translated.text


def main():
    text = input("Enter the text to translate: ")

    source_language = "en"

    dest_language = input("Enter the destination language (e.g., 'fr' for French, 'es' for Spanish): ")

    translated_text = translate_text(text, source_language, dest_language)
    print("Translated text:", translated_text)


if __name__ == "__main__":
    translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)
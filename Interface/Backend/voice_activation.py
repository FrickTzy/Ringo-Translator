import speech_recognition as sr
from .romaji_converter import RomajiConverter


class VoiceActivation:
    language_converter = {
        "Jap": "ja-JP"
    }

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.romaji_converter = RomajiConverter()
        self.word = ""

    def change_lang(self, language) -> str:
        if language != "en-US":
            return self.language_converter.get(language, "en-US")

    def voice(self, language="en-US") -> str:
        language = self.change_lang(language)
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print('listening...')
            audio = self.recognizer.listen(source)
            return self.voice_conditions(audio, language)

    def voice_conditions(self, audio, language) -> str:
        try:
            self.word = self.recognizer.recognize_google(audio, language=language)
            if language == "ja-JP":
                return self.romaji_convert(self.word)
            return self.word
        except sr.UnknownValueError:
            self.word = "couldn't understand it"
            return self.word

        except sr.RequestError:
            self.word = "couldn't connect to google"
            return self.word
        finally:
            print(self.word)

    def romaji_convert(self, japanese_text) -> str:
        return self.romaji_converter.convert(japanese_text)

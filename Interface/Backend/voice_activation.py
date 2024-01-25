import speech_recognition as sr
from threading import Thread
from .romaji_converter import RomajiConverter


class VoiceActivation:
    language_converter = {
        "Japanese": "ja-JP",
        "English": "en-US",
    }

    def __init__(self, result_label, translator, mic_logo, mic_button, entry):
        self.recognizer = sr.Recognizer()
        self.romaji_converter = RomajiConverter()
        self.result_label = result_label
        self.__entry_elements = entry
        self.__mic_logo = mic_logo
        self.__mic_button = mic_button
        self.translator = translator
        self.word = ""

    def change_lang(self, language) -> str:
        if language != "en-US":
            return self.language_converter.get(language, "en-US")

    def voice(self, language="en-US") -> None:
        language = self.change_lang(language)
        Thread(target=self.__use_mic, args=(language,)).start()

    def __use_mic(self, language):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print('\nlistening...')
            audio = self.recognizer.listen(source)
            self.voice_conditions(audio, language)

    def voice_conditions(self, audio, language) -> None:
        try:
            self.word = self.recognizer.recognize_google(audio, language=language)
            self.__entry_elements.set_text(text=self.word)
            self.translator.translate_mic_result(word=self.word)
            return
        except sr.UnknownValueError:
            self.word = "Couldn't understand it"
        except sr.RequestError:
            self.word = "Couldn't connect to Google"
        finally:
            print(self.word)
        self.result_label.config(text=self.word, fg="#757575")
        self.__mic_button.config(image=self.__mic_logo)

    def romaji_convert(self, japanese_text) -> str:
        return self.romaji_converter.convert(japanese_text)

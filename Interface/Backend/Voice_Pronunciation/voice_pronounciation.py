from gtts import gTTS
from pygame import mixer
import os

FOLDER_PATH = "Backend/Voice_Pronunciation/Cache/"


class VoicePronunciation:
    __FOLDER_PATH = FOLDER_PATH
    __VOLUME = 1

    def __init__(self):
        self.__pronunciation_fetcher = PronunciationFetcher()
        self.__fetched_pronunciation_sounds = {}

    def play_pronunciation(self, japanese_character):
        directory_path = f"{self.__FOLDER_PATH}{japanese_character}.mp3"
        if not os.path.exists(directory_path):
            self.__pronunciation_fetcher.download_hiragana_audio(japanese_character=japanese_character)
        if japanese_character not in self.__fetched_pronunciation_sounds:
            self.__append_fetched_sounds(japanese_character=japanese_character, path=directory_path)
        self.__play_sound(japanese_character=japanese_character)

    def set_language(self, language):
        self.__pronunciation_fetcher.change_language(language=language)

    def __append_fetched_sounds(self, japanese_character, path):
        self.__fetched_pronunciation_sounds[japanese_character] = mixer.Sound(path)

    def __play_sound(self, japanese_character):
        mixer.Channel(2).set_volume(self.__VOLUME)
        mixer.Channel(2).stop()
        mixer.Channel(2).play(self.__fetched_pronunciation_sounds[japanese_character])

    def clear_cache(self):
        self.__pronunciation_fetcher.clear_cache()


class PronunciationFetcher:
    __FOLDER_PATH = FOLDER_PATH
    __language_converter = {
        "Japanese": "ja",
        "English": "en",
        "Filipino": "tl",
    }

    def __init__(self):
        self.__text_to_speech = gTTS(lang='ja', text="Default")

    def download_hiragana_audio(self, japanese_character):
        self.__text_to_speech.text = japanese_character
        self.__text_to_speech.save(f"{self.__FOLDER_PATH}{japanese_character}.mp3")

    def clear_cache(self):
        cache_files = os.listdir(self.__FOLDER_PATH)
        for file in cache_files:
            os.remove(f"{self.__FOLDER_PATH}{file}")

    def change_language(self, language):
        current_language = self.__language_converter.get(language, "en")
        self.__text_to_speech.lang = current_language


if __name__ == "__main__":
    hiragana = "みる"
    voice = VoicePronunciation()

from translate import Translator
import pykakasi


class ApiTranslator:
    __convert_lang = {
        "": "en-US",
        "English": "en-US",
        "Filipino": "fil-PH",
        "Japanese": "ja"
    }

    def __init__(self):
        self.__translator = Translator(from_lang="ja", to_lang="en")
        self.__romaji_convertor = pykakasi.Kakasi()

    def translate(self, sentence: str):
        if self.__translator.to_lang == "ja":
            kanji = self.__translator.translate(text=sentence)
            romaji = self.__romaji_convertor.convert(text=kanji)
            return f"{kanji}\n{self.__get_romaji_sentence(romaji=romaji).strip()}"
        else:
            return self.__translator.translate(text=sentence)

    def change_language(self, to_lang, from_lang=""):
        from_lang = self.__convert_lang.get(from_lang, "")
        to_lang = self.__convert_lang.get(to_lang, "")
        self.__translator = Translator(from_lang=from_lang, to_lang=to_lang)

    @staticmethod
    def __get_romaji_sentence(romaji):
        complete_romaji = ""
        for item in romaji:
            if item['orig'] == item['hepburn']:
                continue
            complete_romaji += f"{item.get('hepburn')} "
        return complete_romaji


if __name__ == "__main__":
    translator = ApiTranslator()
    translator.change_language(to_lang="Japanese", from_lang="Filipino")
    print(translator.translate(sentence="Kumain ako ng mansanas"))

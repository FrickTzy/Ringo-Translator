from Translators.Japanese.japanese import jap_translate
from Translators.Filipino.filipino import fil_translate
from Translators.English.english import eng_translate
from Translators.Others.errors import error
from typing import TypeAlias, Literal

Langs: TypeAlias = Literal["Jap", "jap", "Fil", "fil", "Eng", "eng", ""]


class Translate:
    @staticmethod
    def jap(word, language: Langs = ""):
        error(word.lower(), language.title(), "Jap")
        return jap_translate(word, language.title())

    @staticmethod
    def fil(word, language: Langs = ""):
        error(word.lower(), language.title(), "Fil")
        return fil_translate(word, language.title())

    @staticmethod
    def eng(word, language: Langs = ""):
        error(word.lower(), language.title(), "Eng")
        return eng_translate(word, language.title())


if __name__ == "__main__":
    print(Translate.jap("i ate two yellow apples", "eng") + "\n")
    print(Translate.fil("i ate two yellow apples") + "\n")
    print(Translate.eng("ore wa ringo o tabeta"))

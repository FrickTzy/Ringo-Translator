from Translators.Others.dictionary import fil_eng_dict as fil_dict, \
    jap_eng_dict as jap_dict
from Translators.Others.language_class import Language, Functions

Lang_dict = {
    "Jap": jap_dict,
    "Fil": fil_dict,
}


class VarAdd(Language):
    def __init__(self):
        super().__init__()
        self.filler_an = ""

    def add_name(self, name, gender):
        self.name += name.title()
        if gender == "F":
            self.name = f"Ms. {self.name} "
        else:
            self.name = f"Mr. {self.name} "

    def add_filler(self):
        self.noun_name_add()
        self.add_filler_an()

    def add_filler_an(self):
        if self.verb and self.food:
            if self.starts_with_vowel(self.food):
                self.filler_an = "an "
            else:
                self.filler_an = "a "

    def adding(self) -> str:
        self.add_filler()
        self.final += (self.season + self.time + self.greeting + self.noun +
                       self.adjective +
                       self.numbering + self.color + self.thing +
                       self.body + self.verb + self.filler_an + self.food +
                       self.feelings + self.noun2)
        return self.final

    @staticmethod
    def starts_with_vowel(word: str) -> bool:
        vowels = ("a", "i", "u", "e", "o")
        if word.lower().startswith(vowels):
            return True
        return False


def eng_translate(sentences, language=""):
    lang_dict: dict = Lang_dict.get(language, Lang_dict)
    with_lang = False if lang_dict is Lang_dict else True
    return Functions.main_translate(sentences, lang_dict, VarAdd, with_lang)


if __name__ == "__main__":
    print(eng_translate("kurt wa ringo o tabeta", ""))

from Translators.Others.dictionary import jap_fil_dict as jap_dict, \
    eng_fil_dict as eng_dict
from Translators.Others.language_class import Language, Functions

Lang_dict = {
    "Eng": eng_dict,
    "Jap": jap_dict
}

Vowels = ["a", "e", "i", "o", "u"]


class VarAdd(Language):
    def __init__(self):
        super().__init__()
        self.filler_ng = ""
        self.filler_na = ""
        self.si = ""

    def add_name(self, name, gender):
        self.name += f"{name.title()} "
        self.si += "si "

    def add_filler(self):
        if self.verb != "" and self.food != "":
            self.filler_ng = "ng "
        if self.feelings != "" and self.noun != "":
            if self.noun == "Ako":
                self.noun = "'ko"
        if self.color and (self.noun or self.food):
            if (color := self.color.rstrip())[-1] in Vowels:
                self.color = f"{color}ng "
            else:
                self.filler_na = "na "
        self.noun_name_add()

    def adding(self):
        self.add_filler()
        self.final += (self.season + self.time + self.feelings + self.greeting +
                       self.verb + self.si + self.noun + self.noun2 + self.filler_ng +
                       self.adjective + self.numbering + self.color + self.filler_na +
                       self.food + self.thing + self.body)
        return self.final


def fil_translate(sentences, language=""):
    lang_dict: dict = Lang_dict.get(language, Lang_dict)
    with_lang = False if lang_dict is Lang_dict else True  # This is False if there is no specified language, else True
    return Functions.main_translate(sentences, lang_dict, VarAdd, with_lang)


if __name__ == "__main__":
    print(fil_translate("i ate two red apple", "Eng"))

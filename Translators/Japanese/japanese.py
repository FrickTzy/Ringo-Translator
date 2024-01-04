from Translators.Japanese.hiragana_converter import hiragana_converter
from Translators.Others.dictionary import eng_jap_dict as eng_dict, \
    fil_jap_dict as fil_dict
from Translators.Others.language_class import Language, Functions

Lang_dict = {
    "Eng": eng_dict,
    "Fil": fil_dict,
}


class VarAdd(Language):
    def __init__(self):
        super().__init__()
        self.filler_wa, self.filler_ga, self.filler_wo, self.filler_no = "", "", "", ""

    def add_name(self, name, gender):
        self.name += name.title()
        if gender == "F":
            self.name += "-chan "
        else:
            self.name += "-kun "

    def add_filler(self):
        if self.noun and self.feelings:
            self.filler_ga = "ga "
        if self.numbering != "" and (self.food != "" or self.thing != ""):
            self.filler_no = "no "
        self.noun_name_add()
        self.filler_wa_add()
        self.filler_wo_add()

    def filler_wo_add(self):
        if self.noun and self.verb:
            self.filler_wo = "o "

    def filler_wa_add(self):
        if self.noun and (self.food or self.thing or self.numbering or self.feelings):
            self.filler_wa += "wa "

    def adding(self):
        self.add_filler()
        self.final += (self.questions + self.season + self.time + self.greeting + self.noun +
                       self.filler_wa + self.noun2 + self.adjective +
                       self.numbering +
                       self.filler_no + self.pronoun + self.color + self.food + self.thing +
                       self.body + self.filler_wo + self.verb + self.filler_ga +
                       self.feelings)
        self.final = self.final.strip()
        self.final += (self.question_mark + "\n" + hiragana_converter(self.final.lower()))
        return self.final


def jap_translate(sentences, language=""):
    lang_dict: dict = Lang_dict.get(language, Lang_dict)
    with_lang = False if lang_dict is Lang_dict else True  # This is False if there is no specified language, else True
    return Functions.main_translate(sentences, lang_dict, VarAdd, with_lang)


if __name__ == "__main__":
    print(jap_translate("i hate this", ""))

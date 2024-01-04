from Translators.Others.dictionary import eng_jap_dict as eng_dict, \
    fil_jap_dict as fil_dict, jap_eng_dict as jap_dict

LangDict = {
    "Fil": fil_dict,
    "Eng": eng_dict,
    "Jap": jap_dict

}


def check_all_dictionaries(word, targeted_language, language):
    for lang, lang_dict in LangDict.items():
        for types in LangDict[lang]:
            if word in LangDict[lang][types]:
                if language and language != lang:
                    raise LanguageNotMatching
                if lang == targeted_language:
                    raise SameLanguageError
                return " "
    return ''


def error(wordz, language, targeted_language):
    language_list = ["Eng", "Jap", "Fil", ""]
    if language not in language_list:
        raise UnknownLanguageError
    elif language == targeted_language:
        raise SameLanguageError
    else:
        emp = ""
        other = ""
        dictz = LangDict.get(language, "")
        for word in wordz.split():
            other += check_all_dictionaries(word, targeted_language, language)
            for Dict in dictz:
                if word in dictz[Dict]:
                    emp += " "
        if other == "":
            raise UnknownWordError
        if emp == "" and language != "":
            raise LanguageNotMatching


class UnknownLanguageError(Exception):
    def __init__(self):
        self.message = "The language is unknown"
        super().__init__(self.message)


class UnknownWordError(Exception):
    def __init__(self):
        self.message = "The input word is unknown"
        super().__init__(self.message)


class LanguageNotMatching(Exception):
    def __init__(self):
        self.message = "The input does not match the language"
        super().__init__(self.message)


class SameLanguageError(Exception):
    def __init__(self):
        self.message = "Language is the same as the targeted language"
        super().__init__(self.message)

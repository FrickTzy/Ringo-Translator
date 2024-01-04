from abc import ABC, abstractmethod
from Translators.Others.dictionary import names


class Language(ABC):
    def __init__(self):
        self.noun, self.noun2, self.verb, self.feelings, self.food = "", "", "", "", ""
        self.numbering, self.thing, self.greeting, self.color = "", "", "", ""
        self.body, self.time, self.season, self.adjective = "", "", "", ""
        self.name, self.pronoun, self.questions = "", "", ""
        self.final, self.question_mark = "", ""

    def add_noun(self, word):
        if self.noun != "":
            self.noun2 += word.title()
        else:
            self.noun += word.title()

    def add_verb(self, word):
        self.verb += word.title()

    def add_feelings(self, word):
        self.feelings += word.title()

    def add_food(self, word):
        self.food += word.title()

    def add_thing(self, word):
        self.thing += word.title()

    def add_numbering(self, word):
        self.numbering += word.title()

    def add_greeting(self, word):
        self.greeting += word.title()

    def add_body(self, word):
        self.body += word.title()

    def add_time(self, word):
        self.time += word.title()

    def add_season(self, word):
        self.season += word.title()

    def add_adjective(self, word):
        self.adjective += word.title()

    def add_color(self, word):
        self.color += word.title()

    def add_name(self, name, gender):
        self.name += f"{name.title()} "

    def add_pronoun(self, word):
        self.pronoun += word

    def add_questions(self, word):
        self.questions += word.title()
        self.question_mark = "?"

    def dict_var(self, typez, word):
        var_dict: dict = {
            "noun": self.add_noun,
            "verb": self.add_verb,
            "feelings": self.add_feelings,
            "food": self.add_food,
            "numbering": self.add_numbering,
            "thing": self.add_thing,
            "greeting": self.add_greeting,
            "body": self.add_body,
            "time": self.add_time,
            "season": self.add_season,
            "adjective": self.add_adjective,
            "color": self.add_color,
            "pronoun": self.add_pronoun,
            "questions": self.add_questions,
        }
        var_dict.get(typez, "")(word)

    @abstractmethod
    def add_filler(self):
        pass

    def noun_name_add(self):
        if self.noun and self.name:
            self.noun2 = self.name
        elif not self.noun and self.name:
            self.noun = self.name


class Functions:
    @staticmethod
    def remove_filler_s(word: str, types: dict, lang: dict):
        remove_s = word.removesuffix("s")
        remove_es = word.removesuffix("es")
        remove_list = [remove_s, remove_es]
        for word_remove in remove_list:
            if word_remove in lang[types]:
                return word_remove
        return False

    @classmethod
    def name_find(cls, word, var_add):
        if word in names:
            name, gender = names.get(word)
            var_add.add_name(name, gender)

    @classmethod
    def translate_without_lang(cls, word, var_add, lang_dict):
        cls.name_find(word, var_add)
        for lang in lang_dict:
            for types in (dictionary := lang_dict[lang]):
                if s_remove := cls.remove_filler_s(word, types, lang_dict[lang]):
                    word = s_remove
                if word in lang_dict[lang][types]:
                    cls.class_add(var_add, dictionary, word, types)

    @classmethod
    def translate_with_lang(cls, word, var_add, lang_dict):
        cls.name_find(word, var_add)
        for types in lang_dict:
            if s_remove := cls.remove_filler_s(word, types, lang_dict):
                word = s_remove
            if word in lang_dict[types]:
                cls.class_add(var_add, lang_dict, word, types)

    @staticmethod
    def class_add(var_add, dictionary: dict, word, types):
        temp_word = dictionary[types].get(word, '')
        temp_word += ' '
        var_add.dict_var(types, temp_word)

    @classmethod
    def main_translate(cls, sentences, lang_dict, var_add_class, with_lang=True):
        sentences = sentences.lower()
        var_add: var_add_class = var_add_class()
        for word in sentences.split():
            if not with_lang:
                cls.translate_without_lang(word, var_add, lang_dict)
            else:
                cls.translate_with_lang(word, var_add, lang_dict)

        return var_add.adding()

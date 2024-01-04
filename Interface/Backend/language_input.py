from Translators.translator import Translate
from Translators.Others.errors import SameLanguageError, UnknownWordError, \
    LanguageNotMatching
from .api_translate import ApiTranslator


class Language:
    def __init__(self, elements, options):
        self.elements = elements
        self.__options = options
        self.__api_translator = ApiTranslator()
        self.convert_lang = {
            "Auto": "",
            "English": "Eng",
            "Filipino": "Fil",
            "Japanese": "Jap"
        }

        self.convert_lang_to = {
            "English": Translate.eng,
            "Filipino": Translate.fil,
            "Japanese": Translate.jap
        }

    def change_lang(self, event):
        self.elements.variables.lang.set(self.elements.misc.drop_down_for_input.get())
        self.translate_result()

    def change_lang_result(self, event):
        self.elements.variables.lang_result.set(self.elements.misc.drop_down_for_result.get())
        self.translate_result()

    def translate_result(self, event=None):
        if self.__options.using_api:
            self.__translate_result_using_api()
        else:
            self.__translate_result_using_dictionary()

    def __translate_result_using_dictionary(self):
        lang_drop_down = self.convert_lang.get(self.elements.variables.lang.get(), "")
        word = self.elements.entries.input_entry.get()
        lang_result_drop_down = self.elements.variables.lang_result.get()
        lang_func = self.convert_lang_to.get(lang_result_drop_down)
        if word:
            try:
                translated_result = lang_func(word, lang_drop_down)
            except SameLanguageError:
                translated_result = "Same Language! Please Try Again"
            except UnknownWordError:
                translated_result = "Unknown Word!"
            except LanguageNotMatching:
                translated_result = "The input does not match the language! Please Try Again"
            self.elements.labels.result_label.config(text=translated_result, fg="black")
        else:
            self.elements.labels.result_label.config(text="Translating", fg="#757575")

    def __translate_result_using_api(self):
        translate_from = self.convert_lang.get(self.elements.variables.lang.get(), "")
        word = self.elements.entries.input_entry.get()
        translate_to = self.elements.variables.lang_result.get()
        self.__api_translator.change_language(to_lang=translate_to, from_lang=translate_from)
        if word:
            translated_word = self.__api_translator.translate(word)
            self.elements.labels.result_label.config(text=translated_word, fg="black")
        else:
            self.elements.labels.result_label.config(text="Translating", fg="#757575")


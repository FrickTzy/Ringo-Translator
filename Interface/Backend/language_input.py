from threading import Thread
from Translators.translator import Translate
from Translators.Others.errors import SameLanguageError, UnknownWordError, \
    LanguageNotMatching
from .api_translate import ApiTranslator


class Language:
    def __init__(self, elements, options, mic_image):
        self.elements = elements
        self.__options = options
        self.__api_translator = ApiTranslator()
        self.__mic_button = None
        self.__mic_image = mic_image

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

    def translate_result(self, event=None, word=""):
        if self.__options.using_api:
            Thread(target=self.__translate_result_using_api, kwargs={'word_input': word}).start()
        else:
            self.__translate_result_using_dictionary()

    def __translate_result_using_dictionary(self):
        lang_drop_down = self.elements.variables.lang.get()
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

    def __translate_result_using_api(self, word_input: str):
        translate_from = self.elements.variables.lang.get()
        if translate_from == "Auto":
            translate_from = ""
        word = self.elements.entries.input_entry.get()
        translate_to = self.elements.variables.lang_result.get()
        self.__api_translator.change_language(to_lang=translate_to, from_lang=translate_from)
        self.elements.labels.result_label.config(text="Translating...", fg="#757575")
        if word_input:
            word = word_input
        if word:
            translated_word = self.__api_translator.translate(word)
            self.elements.labels.result_label.config(text=translated_word, fg="black")
        else:
            self.elements.labels.result_label.config(text="Waiting for input...", fg="#757575")

    def translate_mic_result(self, event=None, word=""):
        if self.__options.using_api:
            Thread(target=self.__mic_translate, kwargs={'word_input': word}).start()
        else:
            self.__translate_result_using_dictionary()

    def __mic_translate(self, word_input):
        self.__translate_result_using_api(word_input=word_input)
        self.__mic_button.config(image=self.__mic_image)

    def set_mic_button(self, mic_button):
        self.__mic_button = mic_button



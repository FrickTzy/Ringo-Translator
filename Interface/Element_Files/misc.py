from tkinter import Scale, ttk


class MiscElements:
    lang_options = ["Auto", "Japanese", "English", "Filipino"]

    def __init__(self, elements, window, language):
        self.volume_scale = self.make_volume_scale(elements)
        self.volume_scale.set(0.8)
        self.drop_down_for_input = self.make_drop_down_for_input(window)
        self.drop_down_for_result = self.make_drop_down_for_result(window)
        self.drop_down_bind(language)
        self.drop_down_result_bind(language)

    def place_misc(self) -> None:
        self.drop_down_for_input.place(x=40, y=250)
        self.drop_down_for_result.place(x=40, y=400)

    def make_drop_down_for_result(self, window) -> ttk.Combobox:
        return ttk.Combobox(window,
                            values=self.lang_options[1::])

    def make_drop_down_for_input(self, window) -> ttk.Combobox:
        return ttk.Combobox(window,
                            values=self.lang_options)

    def drop_down_bind(self, language) -> None:
        self.drop_down_for_input.current(0)
        self.drop_down_for_input.bind("<<ComboboxSelected>>", language.change_lang)

    def drop_down_result_bind(self, language) -> None:
        self.drop_down_for_result.current(0)
        self.drop_down_for_result.bind("<<ComboboxSelected>>", language.change_lang_result)

    @staticmethod
    def make_volume_scale(elements) -> Scale:
        return Scale(elements.frames.music_frame,
                     from_=1,
                     to=0,
                     length=70,
                     resolution=0.1,
                     fg="white",
                     background="#2b0342",
                     troughcolor="white",
                     bd=0,
                     highlightthickness=0,
                     sliderrelief='flat',
                     sliderlength=12
                     )

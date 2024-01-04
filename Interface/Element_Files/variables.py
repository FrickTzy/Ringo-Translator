from tkinter import StringVar, ttk


class Variables:
    def __init__(self, music, misc):
        self.song_name = StringVar()
        self.lang = StringVar()
        self.lang_result = StringVar()
        self.style = ttk.Style()
        self.style_config()
        self.set_var(music, misc)

    def style_config(self):
        self.style.theme_use("clam")
        self.style.configure('TCombobox',
                             background="white",
                             fieldbackground="white",

                             foreground="black",
                             darkcolor="black",
                             selectbackground="black",
                             lightcolor="black",
                             )

    def set_var(self, music, misc):
        self.lang.set("Auto")
        self.song_name.set(music.set_song_title())
        self.lang_result.set(misc.drop_down_for_result.get())

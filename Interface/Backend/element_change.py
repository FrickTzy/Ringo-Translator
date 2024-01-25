from tkinter import END


class ElementChange:
    switch: str = ""
    vol_repeat: str
    scale_on: bool = False

    def __init__(self, window, elements, backend):
        self.window = window
        self.elements = elements
        self.backend = backend

    def change_song_name(self, var: bool = False):
        if var:
            self.elements.variables.song_name.set(self.backend.music.set_song_title())
        else:
            if self.backend.music.switch != self.switch:
                self.elements.variables.song_name.set(self.backend.music.set_song_title())
                self.switch = self.backend.music.switch
                self.window.update()

    def change_logo(self):
        if self.backend.music.play:
            self.elements.buttons.pause_button.config(image=self.backend.logos.pause_image)
        else:
            self.elements.buttons.pause_button.config(image=self.backend.logos.play_image)

    def change_vol(self):
        self.backend.music.change_volume(self.elements.misc.volume_scale.get())
        self.vol_repeat = self.window.after(10, self.change_vol)

    def show_scale(self):
        if self.scale_on:
            self.elements.misc.volume_scale.place_forget()
            self.scale_on = False
            self.window.unbind("<Up>")
            self.window.unbind("<Down>")
            self.window.after_cancel(self.vol_repeat)
        else:
            self.elements.misc.volume_scale.place(x=210, y=-1)
            self.scale_on = True
            self.window.bind("<Up>", lambda eventz: self.elements.misc.volume_scale.set(
                self.elements.misc.volume_scale.get() + 0.1))
            self.window.bind("<Down>", lambda eventz: self.elements.misc.volume_scale.set(
                self.elements.misc.volume_scale.get() - 0.1))
            self.change_vol()

    def shortcuts(self):
        not_empty = self.elements.entries.input_entry.get()
        if not_empty:
            if self.elements.entries.input_entry.get() == " ":
                self.elements.entries.input_entry.delete(0, END)
            self.window.unbind("<Right>")
            self.window.unbind("<Left>")
            self.window.unbind("<space>")

        else:
            self.window.bind("<Right>", lambda event: [self.backend.music.change_music(self.window, True),
                                                       self.change_song_name(True), self.change_logo()])
            self.window.bind("<Left>", lambda event: self.backend.music.change_music(self.window, False)),
            self.window.bind("<Left>", lambda event: [self.backend.music.change_music(self.window, False),
                                                      self.change_song_name(True), self.change_logo()])
            self.window.bind("<space>", lambda event: [self.backend.music.play_music(),
                                                       self.change_logo()])

        self.window.after(6, lambda: [self.shortcuts(), self.backend.music.music_que(), self.change_song_name()])

    def voice_activate(self, event=None):
        self.elements.buttons.mic_button.config(image=self.backend.logos.mic_on_image)
        self.elements.labels.result_label.config(text="Listening...", fg="#757575")
        self.window.update()
        self.__voice_act()

    def __voice_act(self):
        self.elements.voice_activation.voice(language=self.elements.variables.lang.get())

    def change_input(self, result):
        self.elements.entries.input_entry.delete(0, END)
        self.elements.entries.input_entry.insert(END, result)
        self.elements.language.translate_result()
        self.elements.buttons.mic_button.config(image=self.backend.logos.mic_image)

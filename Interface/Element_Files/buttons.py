from tkinter import Button


class ButtonElements:
    def __init__(self, element, window, backend):
        self.translate_button = self.make_translate_button(window, element)
        self.pause_button = self.make_pause_button(element, backend)
        self.next_button = self.make_next_button(window, element, backend)
        self.prev_button = self.make_prev_button(window, element, backend)
        self.volume_button = self.make_volume_button(element, backend)
        self.mic_button = self.make_voice_act_button(window, backend, element)
        self.pronunciation_button = self.make_pronunciation_button(window, backend, element)

    def place_buttons(self) -> None:
        self.next_button.place(x=99, y=22)
        self.prev_button.place(x=20, y=22)
        self.pause_button.place(x=61, y=22)
        self.volume_button.place(x=250, y=-9)
        self.translate_button.place(x=744, y=290)
        self.translate_button.place(x=744, y=290)
        self.mic_button.place(x=190, y=245)
        self.pronunciation_button.place(x=190, y=395)

    @staticmethod
    def make_translate_button(window, element) -> Button:
        return Button(window,
                      text="Translate",
                      command=element.language.translate_result,
                      borderwidth=3,
                      font=("Ariel", 8),
                      relief="solid",
                      fg="black",
                      bg="white",
                      activeforeground="#757575",
                      width=35, height=5)

    @staticmethod
    def make_pause_button(element, backend) -> Button:
        return Button(element.frames.music_frame,
                      image=backend.logos.pause_image,
                      command=lambda: [backend.music.play_music(),
                                       element.element_change.change_logo()],
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342", )

    @staticmethod
    def make_next_button(window, elements, backend) -> Button:
        return Button(elements.frames.music_frame,
                      image=backend.logos.next_image,
                      command=lambda: [backend.music.change_music(window, True),
                                       elements.element_change.change_song_name(True),
                                       elements.element_change.change_logo()],
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342",
                      )

    @staticmethod
    def make_prev_button(window, elements, backend) -> Button:
        return Button(elements.frames.music_frame,
                      image=backend.logos.previous_image,
                      command=lambda: [backend.music.change_music(window, False),
                                       elements.element_change.change_song_name(True),
                                       elements.element_change.change_logo()],
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342",
                      )

    @staticmethod
    def make_volume_button(elements, backend) -> Button:
        return Button(elements.frames.music_frame,
                      image=backend.logos.volume_image,
                      command=elements.element_change.show_scale,
                      bg="#2b0342",
                      bd=0,
                      activebackground="#2b0342", )

    @staticmethod
    def make_voice_act_button(window, backend, elements) -> Button:
        return Button(window,
                      image=backend.logos.mic_image,
                      command=elements.element_change.voice_activate,
                      bg="#6f5ee0",
                      bd=0,
                      activebackground="#6f5ee0", )

    @staticmethod
    def make_pronunciation_button(window, backend, elements) -> Button:
        return Button(window,
                      image=backend.logos.pronunciation_off_image,
                      command=elements.element_change.pronunciation,
                      bg="#6f5ee0",
                      bd=0,
                      activebackground="#6f5ee0", )

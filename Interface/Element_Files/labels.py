from tkinter import Label


class LabelElements:
    def __init__(self, elements, window, backend):
        self.song_title = self.make_song_title(elements)
        self.logo_label = self.make_logo_label(elements, backend.logos)
        self.result_label = self.make_result_label(window)

    def place_labels(self):
        self.song_title.place(x=0, y=1)
        self.logo_label.place(x=-20, y=-53)
        self.result_label.place(x=40, y=290)

    @staticmethod
    def make_song_title(elements) -> Label:
        return Label(elements.frames.music_frame, textvariable=elements.variables.song_name, bg="#2b0342", fg="white",
                     font=("Ariel", 15),
                     width=14,
                     anchor="n")

    @staticmethod
    def make_logo_label(elements, logos) -> Label:
        return Label(elements.frames.top_frame, image=logos.logo_image, bg="#2b0342")

    @staticmethod
    def make_result_label(window):
        return Label(window,
                     width=96,
                     height=5,
                     borderwidth=3,
                     relief="solid",
                     text="Waiting for input...",
                     fg="#757575",
                     )

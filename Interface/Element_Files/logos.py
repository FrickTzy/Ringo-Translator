from tkinter import PhotoImage


class Logos:
    def __init__(self):
        self.logo_image = PhotoImage(file="Images\\TranslatorLogo.png")
        self.pause_image = PhotoImage(file="Images\\PauseButton.png")
        self.play_image = PhotoImage(file="Images\\PlayButton.png")
        self.next_image = PhotoImage(file="Images\\NextButton.png")
        self.previous_image = PhotoImage(file="Images\\PreviousButtonz.png")
        self.volume_image = PhotoImage(file="Images\\Volume.png")
        self.mic_image = PhotoImage(file="Images\\Mic.png")
        self.mic_on_image = PhotoImage(file="Images\\Mic_on.png")

from tkinter import Frame


class FrameElements:
    def __init__(self, main_cls):
        self.top_frame = self.make_top_frame(main_cls)
        self.music_frame = self.make_music_frame(self.top_frame)

    def place_frames(self) -> None:
        self.top_frame.place(x=0, y=0)
        self.music_frame.place(x=680, y=12)

    @staticmethod
    def make_top_frame(window) -> Frame:
        return Frame(window, bg="#2b0342", width=1000, height=90)

    @staticmethod
    def make_music_frame(top_frame) -> Frame:
        return Frame(top_frame, width=400, height=100, bg="#2b0342")

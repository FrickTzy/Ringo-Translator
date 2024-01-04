from tkinter import PhotoImage, Tk


class Window:
    def __init__(self, name: str, width: int = 1000, height: int = 600, resizable: bool = False,
                 logo: str = "Images\\Ringo-chan_png.png", bg_color: str = "#6f5ee0"):
        self.window = Tk()
        self.logo = PhotoImage(file=logo)
        self.window.title(name)
        self.window.geometry(f"{width}x{height}")
        self.window.config(bg=bg_color)
        self.window.iconphoto(True, self.logo)
        self.window.resizable(resizable, resizable)

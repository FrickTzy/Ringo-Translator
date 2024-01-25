from tkinter import Entry, END


class EntryElements:
    def __init__(self, window, language):
        self.input_entry = self.make_input_entry(window)
        self.bind_entry(language)

    def set_text(self, text):
        self.input_entry.delete(0, END)
        self.input_entry.insert(0, text)

    @staticmethod
    def make_input_entry(window) -> Entry:
        return Entry(window,
                     bg="white",
                     font=("Calibri", 50),
                     width=27,
                     borderwidth=3,
                     relief="solid",
                     )

    def bind_entry(self, language) -> None:
        self.input_entry.bind("<Return>", language.translate_result)

    def place_entry(self):
        self.input_entry.place(x=40, y=140)

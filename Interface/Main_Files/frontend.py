from Interface.Element_Files import *
from Interface.Backend import ElementChange, Language


class Elements:
    def __init__(self, main_window, backend):
        self.frames = FrameElements(main_window)
        self.language = Language(self)
        self.misc = MiscElements(self, main_window, self.language)
        self.entries = EntryElements(main_window, self.language)
        self.element_change = ElementChange(main_window, self, backend)
        self.variables = Variables(backend.music, self.misc)
        self.buttons = ButtonElements(self, main_window, backend)
        self.labels = LabelElements(self, main_window, backend)

    def place_elements(self):
        self.frames.place_frames()
        self.labels.place_labels()
        self.buttons.place_buttons()
        self.entries.place_entry()
        self.misc.place_misc()

from Interface.Element_Files import *
from Interface.Backend import ElementChange, Language, VoiceActivation


class Elements:
    def __init__(self, main_window, backend):
        self.frames = FrameElements(main_window)
        self.language = Language(self, options=backend.options, mic_image=backend.logos.mic_image)
        self.misc = MiscElements(self, main_window, self.language)
        self.entries = EntryElements(main_window, self.language)
        self.element_change = ElementChange(main_window, self, backend)
        self.variables = Variables(backend.music, self.misc)
        self.buttons = ButtonElements(self, main_window, backend)
        self.labels = LabelElements(self, main_window, backend)
        self.voice_activation = VoiceActivation(result_label=self.labels.result_label,
                                                translator=self.language, mic_button=self.buttons.mic_button,
                                                mic_logo=backend.logos.mic_image, entry=self.entries)
        self.language.set_mic_button(mic_button=self.buttons.mic_button)

    def place_elements(self):
        self.frames.place_frames()
        self.labels.place_labels()
        self.buttons.place_buttons()
        self.entries.place_entry()
        self.misc.place_misc()

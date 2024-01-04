from Interface.Backend import *
from Interface.Element_Files import Logos


class Backend:
    def __init__(self):
        self.voice_activation = VoiceActivation()
        self.logos = Logos()
        self.music = Music()

from Interface.Backend import *
import pygame
from Interface.Backend.Voice_Pronunciation import VoicePronunciation
from Interface.Element_Files import Logos


class Backend:
    def __init__(self, window):
        self.logos = Logos()
        self.music = Music()
        self.voice_pronunciation = VoicePronunciation()
        window.protocol("WM_DELETE_WINDOW", lambda: [self.voice_pronunciation.clear_cache(),
                                                     pygame.quit(), window.destroy()])
        self.options = Options(use_api=True)

from Interface.Backend import *
from Interface.Element_Files import Logos


class Backend:
    def __init__(self):
        self.logos = Logos()
        self.music = Music()
        self.options = Options(use_api=True)

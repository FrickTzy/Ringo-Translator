import random
from pygame import mixer
from glob import glob
import os


class SongChecker:
    __SONG_FOLDER_PATH = "/Background Music"

    @classmethod
    def get_all_songs(cls):
        return glob("*.mp3", root_dir=cls.__get_path())

    @classmethod
    def __get_path(cls) -> str:
        return f"{os.getcwd()}{cls.__SONG_FOLDER_PATH}"


class Music:
    x: int = 0
    play: bool = True
    song_name: str = ""
    switch: str = ""

    def __init__(self):
        self.music_list = SongChecker.get_all_songs()
        random.shuffle(self.music_list)
        mixer.init()
        mixer.music.load(os.path.join("Background Music", self.music_list[self.x]))
        mixer.music.play(0)
        self.set_song_title()

    def set_song_title(self) -> str:
        return self.music_list[self.x].removesuffix(".mp3")

    def music_que(self) -> None:
        song_pos = mixer.music.get_pos()
        if int(song_pos) == -1:
            self.next_song_conditions()
            self.switch += " "
            mixer.music.load(os.path.join("Background Music", self.music_list[self.x]))
            mixer.music.play(0)
            self.set_song_title()

    def next_song_conditions(self) -> None:
        if self.x == (len(self.music_list) - 1):
            self.x = -1
        self.x += 1

    def change_music(self, window, direction: bool) -> None:
        if direction:
            self.next_song_conditions()
        else:
            if self.x == 0:
                self.x = (len(self.music_list))
            self.x -= 1
        self.play = True
        mixer.music.stop()
        mixer.music.load(os.path.join("Background Music", self.music_list[self.x]))
        mixer.music.play(0)
        self.set_song_title()

    def play_music(self) -> None:
        if self.play:
            mixer.music.pause()
            self.play = False
        else:
            mixer.music.unpause()
            self.play = True

    @staticmethod
    def change_volume(volume) -> None:
        mixer.music.set_volume(volume)

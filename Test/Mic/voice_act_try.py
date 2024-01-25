import speech_recognition as sr
from time import sleep
from threading import Thread

recognizer = sr.Recognizer()
language = "en-US"

list_of_index = []

def _mic_on():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('listening...')
        audio = recognizer.listen(source)
        word = recognizer.recognize_google(audio, language=language)
        print(word)


def _do_stuff(index):
    sleep(.1)
    print(index)


if __name__ == "__main__":
    for i in range(100):
        Thread(target=_do_stuff, args=(i,)).run()


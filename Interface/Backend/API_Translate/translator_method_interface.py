from abc import ABC, abstractmethod


class TranslatorMethod(ABC):
    @abstractmethod
    def translate(self, sentence: str):
        pass


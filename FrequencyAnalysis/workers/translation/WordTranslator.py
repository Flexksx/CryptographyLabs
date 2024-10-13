from .WordPart import WordPart
from .Word import Word


class WordTranslator:
    def __init__(self, translation_dict: dict) -> None:
        self.__translation_dict = translation_dict

    def translate(self, word: Word) -> str:
        return self.__translate_from_index(word, 0)

    def __translate_from_index(self, word: Word, start: int):
        keys = {
            4: "quadgrams",
            3: "trigrams",
            2: "bigrams",
            1: "letters",
        }
        possible_parts = ["quadgrams", "trigrams", "bigrams", "letters"]
        if start == word.length:
            return ""
        elif start > word.length:
            return None
        for part in possible_parts:

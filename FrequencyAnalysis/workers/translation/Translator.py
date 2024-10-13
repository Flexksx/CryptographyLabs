import string
from .WordTranslator import WordTranslator
from .Word import Word


class Translator:
    def __init__(self, translation_dict: dict, cyphertext: str) -> None:
        self.__translation_dict = translation_dict
        if cyphertext is None:
            self.__cyphertext = ""
        else:
            self.__cyphertext = cyphertext
        self.word_translator = WordTranslator(translation_dict)

    def set_cyphertext(self, cyphertext: str):
        self.__cyphertext = cyphertext

    def translate(self, cyphertext: str = None) -> str:
        if cyphertext is not None:
            self.set_cyphertext(cyphertext)
        words = self.__split_to_words(self.__cyphertext)
        translated_words = self.__translate_words(words)
        translated_text = " ".join([str(word) for word in translated_words])
        return translated_text

    def __split_to_words(self, text: str) -> list:
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator)
        words = cleaned_text.split(" ")
        return [Word(word.strip()) for word in words if word]

    def __translate_words(self, words: list[Word]):
        translated_words = []
        for word in words:
            translated_word = self.word_translator.translate(word)
            translated_words.append(translated_word)
        return translated_words

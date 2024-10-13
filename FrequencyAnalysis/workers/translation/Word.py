from .WordPart import WordPart


class Word:
    def __init__(self, value) -> None:
        self.value = value
        self.length = len(value)
        self.parts = {
            "letters": [],
            "bigrams": [],
            "trigrams": [],
            "quadgrams": []
        }
        self.make_parts()

    def make_parts(self):
        self.parts["letters"] = self.__get_n_grams(1)
        self.parts["bigrams"] = self.__get_n_grams(2)
        self.parts["trigrams"] = self.__get_n_grams(3)
        self.parts["quadgrams"] = self.__get_n_grams(4)

    def __get_n_grams(self, n: int) -> list:
        n_grams = []
        for i in range(self.length - n + 1):
            n_gram = WordPart(self.value[i:i + n], i, i + n - 1)
            n_grams.append(n_gram)
        return n_grams

    def __str__(self) -> str:
        return self.value

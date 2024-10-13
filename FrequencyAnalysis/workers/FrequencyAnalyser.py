class FrequencyAnalyser:
    def __init__(self, text: str) -> None:
        if text is None:
            self.__text = ""
            print("Text is empty")
        else:
            self.__text = text

    def get_text(self) -> str:
        return self.__text

    def set_text(self, text: str):
        self.__text = text

    def analyse(self, text: str) -> dict:
        if self.__text is None:
            self.__text = text
        else:
            if self.__text != text:
                self.__text = text
        return {
            "letters": self.get_letter_frequencies(),
            "bigrams": self.get_bigram_frequencies(),
            "trigrams": self.get_trigram_frequencies(),
            "quadgrams": self.get_quadgram_frequencies()
        }

    def get_letter_frequencies(self) -> dict:
        return self.__get_n_gram_frequencies(1)

    def get_bigram_frequencies(self) -> dict:
        return self.__get_n_gram_frequencies(2)

    def get_trigram_frequencies(self) -> dict:
        return self.__get_n_gram_frequencies(3)

    def get_quadgram_frequencies(self) -> dict:
        return self.__get_n_gram_frequencies(4)

    def __get_n_gram_frequencies(self, n: int) -> dict:
        n_gram_frequencies = {}
        for i in range(len(self.__text) - n + 1):
            n_gram = self.__text[i:i + n]
            if not n_gram.isalpha():
                continue
            n_gram = n_gram.upper()
            if n_gram in n_gram_frequencies:
                n_gram_frequencies[n_gram] += 1
            else:
                n_gram_frequencies[n_gram] = 1
        total_n_grams = sum(n_gram_frequencies.values())
        for n_gram in n_gram_frequencies:
            n_gram_frequencies[n_gram] = (
                n_gram_frequencies[n_gram] / total_n_grams) * 100
        return n_gram_frequencies

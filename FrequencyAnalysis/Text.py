from Word import Word


class Text:
    def __init__(self, value) -> None:
        self.value = value
        self.words = []
        self._generate_words()
        self.length = len(self.words)

    def _generate_words(self):
        for word in self.value.split():
            self.words.append(Word(word))
        return self.words

    def __str__(self) -> str:
        return f'Text with content "{self.value[:100]} of length {self.length}'

    def __repr__(self) -> str:
        return self.value

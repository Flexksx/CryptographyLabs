from WordPart import WordPart


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
        self._generate_parts()

    def _generate_parts(self):
        for i in range(self.length):
            for j in range(i, self.length):
                part = self.value[i:j+1]
                if len(part) == 1:
                    self.parts["letters"].append(WordPart(part))
                elif len(part) == 2:
                    self.parts["bigrams"].append(WordPart(part))
                elif len(part) == 3:
                    self.parts["trigrams"].append(WordPart(part))
                elif len(part) == 4:
                    self.parts["quadgrams"].append(WordPart(part))
                else:
                    continue
        return self.parts

    def __str__(self) -> str:
        return self.value

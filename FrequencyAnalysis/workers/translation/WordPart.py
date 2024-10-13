class WordPart:
    def __init__(self, value: str, start: int, end: int) -> None:
        self.value = value
        self.length = len(value)
        self.order = self.length
        self.start = start
        self.end = end
        self.is_translated = False
        self.translation = None

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f'WordPart("{self.value}", {self.start}, {self.end})'

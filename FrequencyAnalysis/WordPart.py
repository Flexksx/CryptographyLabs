class WordPart:
    def __init__(self, value) -> None:
        self.value = value
        self.length = len(value)
        self.order = self.length
        self.is_translated = False
        self.translation = None

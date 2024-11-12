class AlphabetMatrix:
    def __init__(self) -> None:
        pass

    def _determine_matrix_size(self, alphabet: str) -> tuple:
        alphabet_length = len(alphabet)
        x = int(alphabet_length ** 0.5)
        y = x
        if x * y < alphabet_length:
            y += 1
        if x * y < alphabet_length:
            x += 1
        return x, y

    def _get_empty_matrix(self, x: int, y: int) -> list:
        return [['' for _ in range(x)] for _ in range(y)]

    def _remove_duplicates(self, text: str) -> str:
        seen = set()
        return ''.join([c for c in text if not (c in seen or seen.add(c))])

    def _prepare_alphabet(self, alphabet: str, key: str) -> str:
        alphabet = alphabet.replace("J", "")
        filtered_alphabet = ''.join([c for c in alphabet if c not in key])
        return key + filtered_alphabet

    def _fill_matrix(self, alphabet: str, x: int, y: int) -> list:
        matrix = self._get_empty_matrix(x, y)
        combined_alphabet = sorted(alphabet)
        index = 0
        for i in range(y):
            for j in range(x):
                if index < len(combined_alphabet):
                    matrix[i][j] = combined_alphabet[index]
                    index += 1
                else:
                    break
        return matrix

    def create(self, alphabet: str, normalized_key: str) -> list:
        unique_key = ''.join(sorted(self._remove_duplicates(normalized_key)))
        combined_alphabet = self._prepare_alphabet(alphabet, unique_key)
        x, y = self._determine_matrix_size(combined_alphabet)
        matrix = self._fill_matrix(combined_alphabet, x, y)

        return matrix

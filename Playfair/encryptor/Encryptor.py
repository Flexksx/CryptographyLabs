from alphabets.AlphabetFactory import AlphabetFactory
from encryptor.Preparator import Preparator
from alphabets.AlphabetMatrix import AlphabetMatrix


class Encryptor:
    def __init__(self):
        pass

    def encrypt(self, text: str = None, key: str = None, language_code: str = None) -> str:
        pass

    def _get_matrix(self, language_code: str = None, key: str = None):
        alphabet = AlphabetFactory().create(language_code=language_code)
        matrix_creator = AlphabetMatrix()
        matrix = matrix_creator.create(alphabet=alphabet, key=key)
        return matrix

    def _prepare_key(self, key: str = None):
        return Preparator().prepare_key(key=key)

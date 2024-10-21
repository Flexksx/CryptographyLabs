from collections import Counter
import string
from .translate_by_matches import translate, map_strings_by_frequency


def get_first_letters_frequencies(text: str = None):
    """Parse the first letter of each word in a text and return both the count and the frequency of each letter.

    Args:
        text (str, optional): Cyphertext to analyse. Defaults to None.

    Returns:
        dict[str, dict]: A dictionary containing both the count and frequency of each letter.
    """
    if text is None:
        raise ValueError("No text provided")
    first_letters = [word[0].upper() for word in text.split(
        " ") if word[0] in string.ascii_letters]
    times_letter_appears = Counter(first_letters)
    total_letters = len(first_letters)
    letter_info = {letter: {'count': count, 'frequency': count / total_letters}
                   for letter, count in times_letter_appears.items()}

    return letter_info


def get_word_parts_frequencies(text: str = None, nr_of_letters: int = None, max_parts: int = None):
    """Get the frequency and count of word parts (n-grams) in the given text.

    Args:
        text (str, optional): Cyphertext to analyze. Defaults to None.
        nr_of_letters (int, optional): The length of each word part. Defaults to None.
        max_parts (int, optional): The maximum number of word parts to return. Defaults to None.

    Returns:
        dict[str, dict]: A dictionary containing both the count and frequency of each word part.
    """
    if text is None:
        raise ValueError("No text provided")
    if nr_of_letters is None:
        raise ValueError("No number of letters provided")

    words = text.split(" ")
    word_parts = [
        word[i:i+nr_of_letters].upper()
        for word in words for i in range(len(word) - nr_of_letters + 1)
        if word[i] in string.ascii_letters
    ]

    total_parts = len(word_parts)
    word_part_counts = Counter(word_parts)

    if max_parts is not None:
        word_part_counts = dict(
            sorted(word_part_counts.items(),
                   key=lambda item: item[1], reverse=True)[:max_parts]
        )

    word_part_info = {
        part: {'count': count, 'frequency': count / total_parts}
        for part, count in word_part_counts.items()
    }

    return word_part_info

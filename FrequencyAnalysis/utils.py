from ENGLISH import ENGLISH_FREQUENCY_ANALYSIS


def get_nr_of_key_in_english(key: str = None):
    if key is None:
        raise ValueError(
            "You should specify what key you want to get the number of.")
    return len(list(ENGLISH_FREQUENCY_ANALYSIS[key].keys()))

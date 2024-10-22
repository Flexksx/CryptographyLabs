from ENGLISH import ENGLISH_FREQUENCY_ANALYSIS


def get_nr_of_key_in_english(key: str = None):
    if key is None:
        raise ValueError(
            "You should specify what key you want to get the number of.")
    return len(list(ENGLISH_FREQUENCY_ANALYSIS[key].keys()))


def get_match_table(matches: list[dict]) -> dict:
    """Convert a list of matches to a dictionary for display in a Streamlit app."""
    return {
        'Cypher String': [match['target']['value'] for match in matches],
        'Cypher Frequency': [match['target']['frequency'] for match in matches],
        'English String': [match['source']['value'] for match in matches],
        'English Frequency': [match['source']['frequency'] for match in matches],
    }

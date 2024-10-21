import re


def translate(text: str, matches: dict) -> str:
    # Create a regex pattern that matches any of the keys
    pattern = re.compile(
        '|'.join(map(re.escape, sorted(matches.keys(), key=len, reverse=True))))

    # Use a lambda function to replace the matched keys with their corresponding values
    translated_text = pattern.sub(lambda match: matches[match.group(0)], text)

    return translated_text


def map_strings_by_frequency(dict1: dict[str, dict[str, float]], dict2: dict[str, dict[str, float]]) -> dict[str, str]:
    """Match the most frequent items between two dictionaries.

    Args:
        dict1 (dict[str, dict[str, float]]): The first dictionary with frequency details.
        dict2 (dict[str, dict[str, float]]): The second dictionary with frequency details.

    Returns:
        dict[str, str]: A mapping from items in dict1 to items in dict2 based on frequency.
    """
    # Debug: print the input dictionaries
    print("dict1:", dict1)
    print("dict2:", dict2)

    # Extract and sort items from dict1 and dict2 by frequency
    sorted_dict1 = sorted(
        dict1.items(),
        key=lambda item: item[1]['frequency'] if isinstance(
            item[1], dict) else 0,
        reverse=True
    )
    sorted_dict2 = sorted(
        dict2.items(),
        key=lambda item: item[1]['frequency'] if isinstance(
            item[1], dict) else 0,
        reverse=True
    )

    # Create the mapping dictionary
    mapping = {}
    min_length = min(len(sorted_dict1), len(sorted_dict2))

    for i in range(min_length):
        key_from_dict1 = sorted_dict1[i][0]  # Get the string from dict1
        # Get the corresponding string from dict2
        key_from_dict2 = sorted_dict2[i][0]
        mapping[key_from_dict1] = key_from_dict2

    return mapping

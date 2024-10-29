import re


def translate(text: str, matches: dict) -> str:
    # Create a regex pattern that matches any of the keys, sorted by length
    pattern = re.compile(
        '|'.join(map(re.escape, sorted(matches.keys(), key=len, reverse=True))),
        re.IGNORECASE  # Make the regex case-insensitive
    )

    def replace_case_sensitive(match):
        # Get the matched string
        matched_str = match.group(0)

        # Get the corresponding replacement from the matches dictionary
        replacement = matches[matched_str.upper()]

        # Check the case of the matched string and wrap replacement in HTML to color it
        if matched_str.isupper():
            colored_replacement = f"<span style='color:red;'>{replacement.upper()}</span>"
        elif matched_str.islower():
            colored_replacement = f"<span style='color:red;'>{replacement.lower()}</span>"
        elif matched_str[0].isupper():
            colored_replacement = f"<span style='color:red;'>{replacement.capitalize()}</span>"
        else:
            colored_replacement = f"<span style='color:red;'>{replacement}</span>"

        return colored_replacement

    # Use the pattern to substitute the matched strings with their replacements
    translated_text = pattern.sub(replace_case_sensitive, text)

    return translated_text


def map_strings_by_frequency(dict1: dict[str, float], dict2: dict[str, dict[str, float]]) -> list[dict]:
    """Match the most frequent items between two dictionaries.

    Args:
        dict1 (dict[str, float]): The first dictionary with frequency details.
        dict2 (dict[str, dict[str, float]]): The second dictionary with frequency details.

    Returns:
        list[dict]: A list of match objects containing source and target details.
    """

    # Convert dict1 to the required format
    dict1_converted = {
        key: {"frequency": value} for key, value in dict1.items()
    }

    # Extract and sort items from dict1_converted and dict2 by frequency
    sorted_dict1 = sorted(
        dict1_converted.items(),
        key=lambda item: item[1]['frequency'],
        reverse=True
    )
    sorted_dict2 = sorted(
        dict2.items(),
        key=lambda item: item[1]['frequency'],
        reverse=True
    )

    # Create the matches list
    matches = []
    min_length = min(len(sorted_dict1), len(sorted_dict2))

    for i in range(min_length):
        source_item = sorted_dict1[i]
        target_item = sorted_dict2[i]

        match = {
            "source": {
                "value": source_item[0],  # Get the string from dict1
                "frequency": source_item[1]['frequency']
            },
            "target": {
                "value": target_item[0],  # Get the string from dict2
                "frequency": target_item[1]['frequency']
            }
        }

        matches.append(match)

    return matches

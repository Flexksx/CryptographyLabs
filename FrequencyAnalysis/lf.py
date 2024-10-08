def get_letter_frequencies(text):
    letter_frequencies = {}
    for letter in text:
        if not letter.isalpha():
            continue
        letter = letter.upper()
        if letter in letter_frequencies:
            letter_frequencies[letter] += 1
        else:
            letter_frequencies[letter] = 1
    total_letters = sum(letter_frequencies.values())
    for letter in letter_frequencies:
        letter_frequencies[letter] = (
            letter_frequencies[letter] / total_letters) * 100
    return letter_frequencies


def get_bigram_frequencies(text):
    bigram_frequencies = {}
    for i in range(len(text) - 1):
        if not text[i].isalpha() or not text[i + 1].isalpha():
            continue
        bigram = text[i].upper() + text[i + 1].upper()
        if bigram in bigram_frequencies:
            bigram_frequencies[bigram] += 1
        else:
            bigram_frequencies[bigram] = 1
    total_bigrams = sum(bigram_frequencies.values())
    for bigram in bigram_frequencies:
        bigram_frequencies[bigram] = (
            bigram_frequencies[bigram] / total_bigrams) * 100
    return bigram_frequencies


def get_trigram_frequencies(text):
    trigram_frequencies = {}
    for i in range(len(text) - 2):
        if not text[i].isalpha() or not text[i + 1].isalpha() or not text[i + 2].isalpha():
            continue
        trigram = text[i].upper() + text[i + 1].upper() + text[i + 2].upper()
        if trigram in trigram_frequencies:
            trigram_frequencies[trigram] += 1
        else:
            trigram_frequencies[trigram] = 1
    total_trigrams = sum(trigram_frequencies.values())
    for trigram in trigram_frequencies:
        trigram_frequencies[trigram] = (
            trigram_frequencies[trigram] / total_trigrams) * 100
    return trigram_frequencies


def get_quadgram_frequencies(text):
    quadgram_frequencies = {}
    for i in range(len(text) - 3):
        if not text[i].isalpha() or not text[i + 1].isalpha() or not text[i + 2].isalpha() or not text[i + 3].isalpha():
            continue
        quadgram = text[i].upper() + text[i + 1].upper() + \
            text[i + 2].upper() + text[i + 3].upper()
        if quadgram in quadgram_frequencies:
            quadgram_frequencies[quadgram] += 1
        else:
            quadgram_frequencies[quadgram] = 1
    total_quadgrams = sum(quadgram_frequencies.values())
    for quadgram in quadgram_frequencies:
        quadgram_frequencies[quadgram] = (
            quadgram_frequencies[quadgram] / total_quadgrams) * 100
    return quadgram_frequencies


def analyse_frequencies(text):
    return {
        "letters": sort_by_frequency(get_letter_frequencies(text)),
        "bigrams": sort_by_frequency(get_bigram_frequencies(text)),
        "trigrams": sort_by_frequency(get_trigram_frequencies(text)),
        "quadgrams": sort_by_frequency(get_quadgram_frequencies(text))
    }


def sort_by_frequency(frequencies):
    return dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))


def match_by_frequencies(first_alphabet_frequency, second_alphabet_frequency):
    first_alphabet = list(sort_by_frequency(first_alphabet_frequency).keys())
    second_alphabet = list(sort_by_frequency(second_alphabet_frequency).keys())
    if len(second_alphabet) > len(first_alphabet):
        second_alphabet = second_alphabet[:len(first_alphabet)]
    return dict(zip(first_alphabet, second_alphabet))


def match_analysed_frequencies(first_alphabet_frequency, second_alphabet_frequency):
    focused_parts = ['letters', 'bigrams', 'trigrams', 'quadgrams']
    result = {}
    for part in focused_parts:
        result[part] = match_by_frequencies(
            first_alphabet_frequency[part], second_alphabet_frequency[part])
    return result


def translate_text(text, origin_frequency_analysis, foreign_frequency_analysis):
    translation = match_analysed_frequencies(
        origin_frequency_analysis, foreign_frequency_analysis)
    words = text.split()
    for i, word in enumerate(words):
        words[i] = translate_word(word, translation)
    # return ''.join(words)


def match_ngram(word, translation, ngram):
    if len(word) < ngram:
        raise ValueError("Word is shorter than the number of ngram")
    result = ""


def translate_word(word, translation):
    translation_keys_intervals = {
        'quadgrams': 4,
        'trigrams': 3,
        'bigrams': 2,
        'letters': 1,
    }
    translation_keys = list(translation_keys_intervals.keys())
    for translation_phase in translation_keys:
        interval = translation_keys_intervals[translation_phase]
        print(translation_phase, interval)
        break

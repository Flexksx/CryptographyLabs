def create_permuted_alphabet(keyword, alphabet_letters):
    print(f"Got permutation key: {keyword}")
    unique_keyword = "".join(sorted(set(keyword), key=keyword.index))
    print(f'Unique keyword: {unique_keyword}')
    permuted_alphabet = list(unique_keyword)
    for letter in alphabet_letters:
        if letter not in permuted_alphabet:
            permuted_alphabet.append(letter)
    new_alphabet = {letter: index for index,
                    letter in enumerate(permuted_alphabet)}
    new_alphabet.update(
        {index: letter for index, letter in enumerate(permuted_alphabet)})

    return new_alphabet

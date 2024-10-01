def encrypt(plaintext, key, alphabet_keys):
    ciphertext = []
    number_keys = [key for key in alphabet_keys.keys() if isinstance(key, int)]
    letter_keys = [key for key in alphabet_keys.keys() if isinstance(key, str)]
    n = len(number_keys)
    for letter in plaintext:
        if letter in letter_keys:
            index = alphabet_keys[letter]
            ciphertext.append(alphabet_keys[(index + key) % n])
        else:
            ciphertext.append(letter)
    return "".join(ciphertext)

def decrypt(ciphertext, key, alphabet_keys):
    plaintext = []
    number_keys = [key for key in alphabet_keys.keys() if isinstance(key, int)]
    letter_keys = [key for key in alphabet_keys.keys() if isinstance(key, str)]
    n = len(number_keys)
    for letter in ciphertext:
        if letter in letter_keys:
            index = alphabet_keys[letter]
            plaintext.append(alphabet_keys[(index - key) % n])
        else:
            plaintext.append(letter)
    
    return "".join(plaintext)
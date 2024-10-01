import argparse
import caesar
import permutation


def print_alphabet(alphabet):
    for key, value in alphabet.items():
        print(f"{key}: {value}")


def caesar_cypher(text, key, permutation_key=None, mode="decrypt"):
    alphabet_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    reference_alphabet = {letter: index for index, letter in enumerate(alphabet_letters)}
    reference_alphabet.update({index: letter for index, letter in enumerate(alphabet_letters)})

    modes = {
        "decrypt": caesar.decrypt,
        "encrypt": caesar.encrypt
    }

    if permutation_key:
        new_alphabet = permutation.create_permuted_alphabet(permutation_key, alphabet_letters)
        return modes[mode](text, key, new_alphabet)
    else:
        return modes[mode](text, key, reference_alphabet)


def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher with optional permutation key")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the text")
    group.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the text")

    parser.add_argument("text", help="Text to encrypt or decrypt")
    parser.add_argument("key", type=int, help="Shift key for Caesar Cipher")
    parser.add_argument("-p", "--permutation_key", help="Keyword to permute the alphabet")

    args = parser.parse_args()

    mode = "encrypt" if args.encrypt else "decrypt"

    result = caesar_cypher(args.text, args.key, args.permutation_key, mode)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()

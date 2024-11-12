from encryptor.Encryptor import Encryptor

encryptor = Encryptor()

text = "Salut, lume! Ce mai faci?"
key = "MYSUPERSTRONGKEY"
language_code = "ro"


encrypted_text = encryptor.encrypt(
    text=text, key=key, language_code=language_code)
print(encrypted_text)

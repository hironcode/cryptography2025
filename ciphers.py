import string


def caesar(plaintext, key: str, encrypt=True):
    plaintext = plaintext.lower()
    alphabet = list(string.ascii_lowercase) + [" "]
    
    if encrypt == True:
        key = int(key)
    else:
        key = -int(key)

    idxs = [alphabet.index(l) for l in plaintext]
    idxs = [(idx+key)%len(alphabet) for idx in idxs]
    return "".join([alphabet[idx] for idx in idxs])


def vigenere(plaintext:str, key:str, encrypt=True):
    plaintext = plaintext.lower()
    alphabet = list(string.ascii_lowercase) + [" "]

    if encrypt is True:
        key = [alphabet.index(l) for l in key]
    else:
        key = [-alphabet.index(l) for l in key]

    # align the length of key to plaintext
    key = key*(len(plaintext)//len(key)) + key[:len(plaintext)%len(key)]
    idxs = [alphabet.index(l) for l in plaintext]
    assert len(key) == len(idxs), (len(key), len(idxs))
    idxs = [(idx+k)%len(alphabet) for idx, k in zip(idxs, key)]
    return "".join([alphabet[idx] for idx in idxs])
    


def encrypt(cipher):
    input_text = input('Enter text to encrypt: ')
    key = input('Enter key: ')
    encrypted = cipher(input_text, key, encrypt=True)
    return encrypted

def decrypt(cipher):
    input_text = input('Enter text to decrypt: ')
    key = input('Enter key: ')
    decrypted = cipher(input_text, key, encrypt=False)
    return decrypted

if __name__ == '__main__':
    encrypted = encrypt(vigenere)
    print(encrypted)
    decrypted = decrypt(vigenere)
    print(decrypted)
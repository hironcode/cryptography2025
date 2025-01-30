import string
import pandas as pd
import os

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

def write_message(sender:str, receiver:str, message:str):
    path = "messages.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        pd.concat(df, pd.DataFrame({'sender': sender, 'receiver': receiver, "message": message}), axis=0, ignore_index=True)
    else:
        df = pd.DataFrame({"sender": [sender], "receiver": [receiver], "message": [message]})

    df.to_csv(path, index=False)


def read_message(sender, receiver):
    path = "messages.csv"
    df = pd.read_csv(path)
    message = df.loc[(df['sender']==sender) & (df['receiver']==receiver), 'message']
    return message
    
def write(cipher, sender, receiver):
    encrypted = encrypt(cipher)
    print(f"Message encrypted: {encrypted}")
    write_message(sender, receiver, encrypted)

def read(cipher, sender, receiver):
    message = read_message(sender, receiver)
    print(f"Message encrypted: {message}")
    decrypted = decrypt(cipher)
    print(decrypted)

if __name__ == '__main__':
    write(caesar, "test1", "test2")
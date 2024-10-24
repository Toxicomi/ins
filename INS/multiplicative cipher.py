LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = (num * key) % 26
            encrypted += LETTERS[num]

    return encrypted

def decrypt(message, key):
    decrypted = ''
    inverse_key = None
    for i in range(26):
        if (key * i) % 26 == 1:
            inverse_key = i
            break

    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = int(num * inverse_key) % 26
            decrypted += LETTERS[num]
    print("Inverse :",decrypted)

    return decrypted

def main():
    message = str(input('Enter your message: '))
    key = int(input('Enter your key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')

    if choice.lower().startswith('e'):
        print(encrypt(message, key))
    else:
        print(decrypt(message, key))

main()

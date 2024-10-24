LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

def additive_encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = (num + key) % 26
            encrypted += LETTERS[num]

    return encrypted

def additive_decrypt(message, key):
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = (num - key) % 26
            decrypted += LETTERS[num]

    return decrypted

def multiplicative_encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = (num * key) % 26
            encrypted += LETTERS[num]

    return encrypted

def multiplicative_decrypt(message, key):
    decrypted = ''
    inverse_key = None
    for i in range(26):
        if (key * i) % 26 == 1:  # Finding multiplicative inverse of key
            inverse_key = i
            break

    if inverse_key is None:
        return "No inverse key exists for the given key."

    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = (num * inverse_key) % 26
            decrypted += LETTERS[num]

    return decrypted

def main():
    message = str(input('Enter your message: ')).lower()
    key = int(input('Enter your key [1 - 25]: '))
    
    cipher_type = input('Choose cipher type - Additive (A) or Multiplicative (M): ').lower()
    choice = input('Encrypt or Decrypt? [E/D]: ').lower()

    if cipher_type == 'a':  # Additive Cipher
        if choice == 'e':
            print("Encrypted message:", additive_encrypt(message, key))
        else:
            print("Decrypted message:", additive_decrypt(message, key))
    elif cipher_type == 'm':  # Multiplicative Cipher
        if choice == 'e':
            print("Encrypted message:", multiplicative_encrypt(message, key))
        else:
            print("Decrypted message:", multiplicative_decrypt(message, key))
    else:
        print("Invalid cipher type selected.")

main()

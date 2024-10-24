LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS.lower()

# Function to compute the modular inverse of 'a' modulo 26
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Affine cipher encryption
def affine_encrypt(message, a, b):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            x = LETTERS.find(chars)
            encrypted += LETTERS[(a * x + b) % 26]
    return encrypted

# Affine cipher decryption
def affine_decrypt(message, a, b):
    decrypted = ''
    a_inv = mod_inverse(a, 26)  # Find the modular inverse of 'a'
    
    if a_inv is None:
        return "Multiplicative inverse for 'a' does not exist."

    for chars in message:
        if chars in LETTERS:
            x = LETTERS.find(chars)
            decrypted += LETTERS[(a_inv * (x - b)) % 26]
    return decrypted

def main():
    message = str(input('Enter your message: ')).lower()
    a = int(input('Enter your multiplicative key [1 - 25]: '))
    b = int(input('Enter your additive key [1 - 25]: '))

    # Ensure the multiplicative key is coprime with 26
    if mod_inverse(a, 26) is None:
        print("Error: The multiplicative key must be coprime with 26.")
        return
    
    choice = input('Encrypt or Decrypt? [E/D]: ').lower()

    if choice == 'e':
        print("Encrypted message:", affine_encrypt(message, a, b))
    elif choice == 'd':
        print("Decrypted message:", affine_decrypt(message, a, b))
    else:
        print("Invalid option selected.")

main()

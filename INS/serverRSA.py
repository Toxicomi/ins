import socket
import random
def modexp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(modexp(char, d, n)) for char in ciphertext])
    return decrypted_message
def generate_keypair(p, q):
    n = p * q
    nn = (p - 1) * (q - 1)
    j = 1
    for i in range(1, n):
        e = nn % i
        if e != 0:
            e = i
            break    
    while True:
        t = (e * j) % nn
        if t == 1:
            d = j
            print(f"Prime Numbers are p= {p} and q= {q}")
            print(f"Private key is {d}")
            break
        j += 1    
    public_key = (e, n)
    private_key = (d, n)    
    return public_key, private_key
def generate_prime():
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    u_n = random.sample(prime, len(prime))
    p, q = u_n[1], u_n[2]
    return p,q
# Key generation
p,q= generate_prime()
public_key, private_key = generate_keypair(p, q)
# Socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.56.1', 8080))
server_socket.listen()
# Wait for a connection
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")
# Send primes to the client
primes_message = f"{p},{q}"
client_socket.send(primes_message.encode())
# Receive and decrypt message
encrypted_message = client_socket.recv(1024).decode()
print("Encrypted message : ",encrypted_message)
ciphertext = [int(char) for char in encrypted_message.split(',')]
decrypted_message = decrypt(ciphertext, private_key)
print("Received and decrypted message:", decrypted_message)
# Clean up
client_socket.close()
server_socket.close()

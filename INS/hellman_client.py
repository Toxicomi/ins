import socket
import random

def generate_key_pair(p, g):
    private_key = int(input("Enter Private key"))
    public_key = pow(g, private_key, p)
    return private_key, public_key

def calculate_shared_secret(private_key, public_key, p):
    return pow(public_key, private_key, p)

# Set up the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.56.1', 8080))

# Diffie-Hellman key exchange
primes_message = client_socket.recv(1024).decode()
p, g = map(int, primes_message.split(','))
print(f"Prime no.: {p} \n value of g: {g}")

alice_private_key, alice_public_key = generate_key_pair(p, g)
print("Public key of A: ",alice_public_key)
client_socket.send(str(alice_public_key).encode())

server_public_key = int(client_socket.recv(1024).decode())
print("Public key of B: ",server_public_key)
shared_secret_alice = calculate_shared_secret(alice_private_key, server_public_key, p)

print("Shared key with B:", shared_secret_alice)

# Close the connection
client_socket.close()

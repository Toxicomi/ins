import socket
import random

# Diffie-Hellman key exchange
def generate_prime():
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    u_n = random.sample(prime, len(prime))
    p, q = u_n[1], u_n[2]
    return p,q

def generate_key_pair(p, g):
    #private_key = random.randint(2, p - 1)
    private_key =int(input("enter key: "))
    public_key = pow(g, private_key, p)
    return private_key, public_key

def calculate_shared_secret(private_key, public_key, p):
    return pow(public_key, private_key, p)



# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.56.1', 8080))
server_socket.listen(1)

print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

p,g= generate_prime()
# Send primes to the client
primes_message = f"{p},{g}"
client_socket.send(primes_message.encode())

bob_private_key, bob_public_key = generate_key_pair(p, g)
print("Public key of b: ",bob_public_key)
client_socket.send(str(bob_public_key).encode())

client_public_key = int(client_socket.recv(1024).decode())
print("Public key of A: ",client_public_key)
shared_secret_bob = calculate_shared_secret(bob_private_key, client_public_key, p)

print("Shared secret key with A:", shared_secret_bob)

# Close the connection
client_socket.close()
server_socket.close()

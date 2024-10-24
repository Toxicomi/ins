import socket
def modexp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result
def encrypt(message, public_key):
    e, n = public_key
    ciphertext = ','.join([str(modexp(ord(char), e, n)) for char in message])
    return ciphertext
def generate_keypair(p, q):
    n=p*q
    nn=(p-1)*(q-1)
    j=1
    for i in range(1,n):
        e=nn%i
        if e!=0:
            e=i
            break 
    while True:
        t=(e*j)%nn
        if t==1:
            d=j
            break
        j+=1
    public_key = (e, n)
    private_key = (d, n) 
    return public_key, private_key
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.56.1', 8080))

# Receive primes from the server
primes_message = client_socket.recv(1024).decode()
p, q = map(int, primes_message.split(','))

# Key generation using received primes
public_key, private_key = generate_keypair(p, q)
print(f"public key is {public_key[0]} ")
message = str(input("Enter Plaintext: "))

# Encrypt and send message
encrypted_message = encrypt(message, public_key)
print("Encrypted Message: ",encrypted_message)
client_socket.send(encrypted_message.encode())
client_socket.close()

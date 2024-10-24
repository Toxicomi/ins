import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Generate RSA private and public keys
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    # Convert keys to PEM format for easy transmission
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_key, private_key_pem, public_key_pem

# Sign the message with RSA private key
def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Server function to handle client messages and send back the signature
def server():
    host = '0.0.0.0'
    port = 192
    
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    private_key, private_key_pem, public_key_pem = generate_rsa_keys()
    
    print("Waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    
    # Send the public key to the client
    conn.send(public_key_pem)
    
    # Receive message from the client
    message = conn.recv(1024)
    print(f"Received message from client: {message.decode()}")
    
    # Sign the message
    signature = sign_message(private_key, message)
    
    # Send signature back to client
    conn.send(signature)
    print(f"Signature sent to client.")
    
    conn.close()

if __name__ == "__main__":
    server()

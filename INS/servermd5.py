import socket
import hashlib

def hash_message(message):
    sha1 = hashlib.sha1(message.encode()).hexdigest()
    md5_ = hashlib.md5(message.encode()).hexdigest()
    return sha1, md5_

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8085))
    server_socket.listen(1)
    print("Server is listening on port...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        
        sha1, md5_ = hash_message(message)
        response = f"SHA-1: {sha1}, MD5: {md5_}"
        client_socket.send(response.encode())
        
        client_socket.close()

start_server()

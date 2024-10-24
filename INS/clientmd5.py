import socket

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8085))
    
    client_socket.send(message.encode())
    
    response = client_socket.recv(1024).decode()
    print(f"Response from server: {response}")
    
    client_socket.close()


message = input("Enter a message to hash: ")
send_message(message)

import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")


while True:
    (client_socket, client_address) = server_socket.accept()
    print("Client connected", client_address)
    while True:
        data = client_socket.recv(1024).decode()
        if data == "exit" or data is None or data == "":
            client_socket.close()
            print("Client disconnected")
            break
        try:
            os.system(data + '.exe')
            client_socket.send("".encode())
        except Exception as e:
            print(e)

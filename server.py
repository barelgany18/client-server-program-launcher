import socket
import os
import pyautogui

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")

while True:
    (client_socket, client_address) = server_socket.accept()
    print("Client connected", client_address)
    while True:
        data = client_socket.recv(1024).decode()
        if data[0] == "q" or data[0] is None:
            client_socket.close()
            print("Client disconnected")
            break
        split_data = data.split("-")
        if data[0] == 'p':
            try:
                os.system(split_data[1] + '.exe')
            except Exception as e:
                print(e)

        elif data[0] == 'c':
            if pyautogui.onScreen(int(split_data[1]), int(split_data[2])):
                pyautogui.click(int(split_data[1]), int(split_data[2]))
            else:
                print("coordinates are not within the screen’s boundaries")
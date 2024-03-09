import functools
import socket
import os
import pyautogui


class Server:
    _connection: socket.socket

    def __init__(self):
        print("Server is up and running")
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, server_ip: str, server_port: int) -> None:
        self._connection.bind((server_ip, server_port))
        self._connection.listen()

    def accept(self) -> (str, str):
        (client_socket, client_address) = self._connection.accept()
        return client_socket, client_address


def recv(client_socket: socket.socket) -> str:
    data = client_socket.recv(1024).decode()
    return data


def run_command(data: str) -> None:
    action, command = data.split('-')
    try:
        os.system(command + '.exe')
    except Exception as e:
        print(e)


def click(data: str) -> None:
    action, x, y = data.split('-')
    if pyautogui.onScreen(int(x), int(y)):
        pyautogui.click(int(x), int(y))


def send_file(data: str) -> None:
    action, file_content, path = data.split("-")
    file = open(path, 'w')
    file.write(file_content)
    file.close()


def main() -> None:
    server = Server()
    server.bind("0.0.0.0", 8820)

    command_mapping = {
        'c': click,
        'p': run_command,
        'f': send_file
    }

    while True:
        (client_socket, client_address) = server.accept()
        print("Client connected", client_address)

        while True:
            data = recv(client_socket)
            if data is None or data == "":
                break
            action = data[0]
            command_mapping[action](data)


if __name__ == '__main__':
    main()

import socket
from typing import Optional


class Client:
    _connection: socket.socket

    def __init__(self):
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, server_ip: str, server_port: int) -> None:
        self._connection.connect((server_ip, server_port))

    def click(self) -> None:
        x = int(input('Enter x coord:'))
        y = int(input('Enter y coord:'))
        self._connection.send(f'c-{x}-{y}'.encode())

    def run_command(self) -> None:
        command = input('Enter command: ')
        self._connection.send(f'p-{command}'.encode())

    def send_file(self) -> None:
        target_file_path = input('Enter target file path: ')
        source_file_path = input('Enter source file path: ')

        # TODO: send the file content to the server and put it in the target path
        # Consider using base64


def main() -> None:
    client = Client()
    client.connect('127.0.0.1', 8820)

    command_mapping = {
        'c': client.click,
        'p': client.run_command,
        'f': client.send_file
    }

    action = ''
    while action != 'q':
        available_actions = ', '.join(command_mapping.keys())
        action = input(f'Enter action to perform ({available_actions}): ')
        if action in command_mapping.keys():
            command_mapping[action]()
        elif action != 'q':
            print(f'{action} is an invalid action')


if __name__ == '__main__':
    main()

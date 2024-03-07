import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820))

while True:
    msg = input("Please enter your message\n")
    my_socket.send(msg.encode())
    if msg == "exit" or msg is None or msg == "":
        break

print("Goodbye")
my_socket.close()

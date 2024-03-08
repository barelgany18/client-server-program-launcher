import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820))

print("p \t Run program")
print("c \t Press coordinates")
print("q \t Quit")
choice = input("Please enter your choice: ")
while choice != 'q':
    if choice == 'p':
        program_name = input("Enter program name: ")
        msg = "p" + "-" + program_name
        my_socket.send(msg.encode())
    elif choice == 'c':
        x_coordinates = input("Enter X coordinates: ")
        y_coordinates = input("Enter Y coordinates: ")
        msg = "c" + "-" + x_coordinates + "-" + y_coordinates
        my_socket.send(msg.encode())

    print("p \t Run program")
    print("c \t Press coordinates")
    print("q \t Quit")
    choice = input("Please enter your choice: ")

print("Goodbye")
my_socket.close()

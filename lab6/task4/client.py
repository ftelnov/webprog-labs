import socket
from threading import Thread

HOST = "localhost"
PORT = 8000


def receive_messages():
    while True:
        data = sock.recv(1024).decode()
        print(data)


with socket.socket() as sock:
    sock.connect((HOST, PORT))
    username = input("Введите свое имя: ")

    thread = Thread(target=receive_messages)
    thread.daemon = True
    thread.start()

    while True:
        user_msg = input()
        user_msg = f"{username}: {user_msg}"
        sock.send(user_msg.encode())

    sock.close()

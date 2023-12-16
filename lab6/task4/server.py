import socket
from threading import Thread


HOST = "localhost"
PORT = 8000
clients = set()


def listen_for_client(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
        except Exception as e:
            # drop client on error.
            print(f"Removing client {sock} due to err: {e}")
            clients.remove(sock)

        # send messages to all other clients.
        for client_socket in clients:
            if client_socket != sock:
                client_socket.send(data.encode())


with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    while True:
        client_socket, _ = sock.accept()
        clients.add(client_socket)
        print(f"Client {client_socket} just joined")
        thread = Thread(target=listen_for_client, args=(client_socket,))
        thread.daemon = True
        thread.start()

    for client_sock in clients:
        client_sock.close()

import socket

HOST = "localhost"
PORT = 3000

BUFSIZE = 1024
ENCODING = "utf-8"
MSG = b"Hello, client"

with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    conn, addr = sock.accept()
    with conn:
        client_msg = conn.recv(BUFSIZE)
        print(client_msg.decode(ENCODING))
        conn.send(MSG)

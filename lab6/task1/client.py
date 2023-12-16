import socket

HOST = "localhost"
PORT = 3000

BUFSIZE = 1024
ENCODING = "utf-8"
MSG = b"Hello, server"

with socket.socket() as sock:
    sock.connect((HOST, PORT))
    sock.send(MSG)
    srv_msg = sock.recv(BUFSIZE)
    print(srv_msg.decode(ENCODING))

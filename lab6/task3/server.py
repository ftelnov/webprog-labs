import socket

HOST = "localhost"
PORT = 8000

with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    conn, addr = sock.accept()
    with conn:
        http_code = b"HTTP/1.1 200 OK"

        with open("index.html", "rb") as f:
            content = f.read()

        headers = {
            "Content-Type": "text/html",
            "Content-Length": str(len(content)),
            "Connection": "close",
        }
        headers = b"\n".join(
            map(lambda pair: f"{pair[0]}: {pair[1]}".encode(), headers.items())
        )

        data = [http_code, headers, b"", content]
        data = b"\n".join(data)

        conn.send(data)

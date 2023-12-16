import socket

HOST = "localhost"
PORT = 3000

equation = input('Введите квадратное уравнение в форме "x*x + b*x + c": ')

with socket.socket() as sock:
    sock.connect((HOST, PORT))

    sock.send(equation.encode())
    response = sock.recv(1024)
    print("Корни:", response.decode("utf-8"))

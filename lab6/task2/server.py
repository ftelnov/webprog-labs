import socket
import math

from sympy.solvers import solve
from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr

HOST = "localhost"
PORT = 3000


def solve_equation(equation):
    x = Symbol("x")
    return solve(parse_expr(equation), x)


with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    conn, addr = sock.accept()
    with conn:
        equation = conn.recv(1024)

        equation = equation.decode()
        result = str(solve_equation(equation))
        conn.send(result.encode())

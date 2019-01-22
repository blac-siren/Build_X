#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 65443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    # conn is new socket object usable to send # and receive data on the connection.
    # address bound to the socket on the other end of the connection
    conn, address = sock.accept()

    with conn:
        print(f"Connected to {address}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


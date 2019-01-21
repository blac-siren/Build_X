#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 64321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))

    sock.listen()
    conn, addrs = sock.accept()

    with conn:
        print(f"Connected to {addrs}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


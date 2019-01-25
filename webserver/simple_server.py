#!/usr/bin/env python
from __future__ import print_function

import socket

HOST, PORT = '', 8000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print("Serving HTTP on port", PORT)

while True:

    client_coonnection, client_address = listen_socket.accept()
    request = client_coonnection.recv(1024).decode()

    print(request)

    response = 'HTTP/1.0 200 OK\n\nHello World'
    client_coonnection.sendall(response.encode())
    client_coonnection.close()

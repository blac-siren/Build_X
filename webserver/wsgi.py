#!/usr/bin/env python3
"""
Implementation of Webserver Gateway Interface (WSGI)
"""

import sys
import socket


class WSGIServer:

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type,
        )
        listen_socket.bind(address)
        listen_socket.listen(self.request_queue_size)
        host, port = listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        self.headers_set = []

    def set_app(sefl, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            self.client_connection, client_address = listen_socket.accept()
            self.handle_one_request()

    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024)
        print(''.join('<{line>}\n'.format(line=line)
                      for line in request_data.splitlines()))
        self.parse_request(request_data)

        env = self.get_environ()
        result = self.set_application(env, self.start_response)
        self.finish_response(result)

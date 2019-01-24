#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback

import libserver

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addrs = sock.accept()
    print(f"Accepted connection from {addrs}")
    conn.setblocking(False)
    message = libserver.Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)


if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "<host><port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Avoid bind() execptiion: OSError [Error 48] Address in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind((host, port))
lsock.listen()
print("Listening on", (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                message = key.data
                try:
                    message.process_events(mask)
                except Exception:
                    print("Main: Error: exception for",
                          f"{message.addrs}:\n{traceback.format_exc()}")
                    message.close()

except KeyboardInterrupt:
    print("Caught keyboard interrupt, Exiting")
finally:
    sel.close()
#!/usr/bin/env python3

import sys
import socket
import selectors
import types

selec = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addrs = sock.accept()
    print(f"Accepted connection from {addrs}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addrs=addrs, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    selec.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to", data.addrs)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing, {repr(data.outb)} to {data.addr}")
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.Af_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()

print(f"Listening on {(host, port)}")

# configure the socket in non-blocking mode.
lsock.setblocking(False)
selec.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = selec.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Keyboard interrupt, exiting")
finally:
    sel.close()


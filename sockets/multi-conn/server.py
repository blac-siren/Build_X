#!/usr/bin/env python3

import socket
import selectors

selec = selectors.DefaultSelector()

#...

lsock = socket.socket(socket.Af_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()

print(f'Listening on {(host, port)}')

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
    print('Keyboard interrupt, exiting')
finally:
    sel.close()

    


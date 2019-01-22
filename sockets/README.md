### Socket Programming.

> For [basic implementation](https://github.com/blac-siren/Build_X/tree/master/sockets/basic) the server will simply echo whatever it receives back to the client.
- The socket address family and protocal will use `socket.AF_INET(IPV4)`
- The port should be and integer from 1-65535 (0 is reserved)

    | Address Family  | Protocal      | Address tuple   |
    | ----------------|:-------------:| ---------------:|
    | __socket.AF_INET__| IPV4        | (host, port)    |
- `SOCK_STREAM` is the socket type for __TCP__, the protocal will use to transport our messages packets in the network.
- `accept()` [__blocks__](#block-calls) and waits for an incoming connection. When the client connects, it returns a pair (*conn*, *address*), where __conn__ is a new socket object usable to send and receive data on th connection, and the __address__ is the address bound to the socket on the other end of the connection.

#### Blocking Calls
A socket function or method that temporarily suspends your application is a blocking call.
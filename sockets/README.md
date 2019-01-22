### Socket Programming.

> For [basic implementation](https://github.com/blac-siren/Build_X/tree/master/sockets/basic) the server will simply echo whatever it receives back to the client.
- The socket address family and protocal will use `socket.AF_INET`

    | Address Family  | Protocal      | Address tuple   |
    | ----------------|:-------------:| ---------------:|
    | __socket.AF_INET__| IPV4        | (host, port)    |
- `SOCK_STREAM` is the socket type for __TCP__, the protocal will use to transport our messages packets in the network.
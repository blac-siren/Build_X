### Socket Programming.

> For [basic implementation](https://github.com/blac-siren/Build_X/tree/master/sockets/basic) the server will simply echo whatever it receives back to the client.
- The socket address family and protocal will use `socket.AF_INET(IPV4)`
- The port should be and integer from 1-65535 (0 is reserved)

    | Address Family  | Protocal      | Address tuple   |
    | ----------------|:-------------:| ---------------:|
    | __socket.AF_INET__| IPV4        | (host, port)    |
- `SOCK_STREAM` is the socket type for __TCP__, the protocal used to transport our messages packets in the network.
- `accept()` [block](#blocking-calls) and waits for an incoming connection. When the client connects, it returns a pair `(conn, address)`, where __conn__ is a new socket object usable to send and receive data on th connection, and the __address__ is the address bound to the socket on the other end of the connection
- It is imperative to understand that the new socket object from `accept()` is the one that is used to communicate with the client and it's distinct from listening socket that the server is using to accept new connection.
- `socket.recv(bufsize)` receive data from socket. The return value is a byte object representing the data received. The maximum amount of data to be received at once is specified by `bufsize`.
- `conn.recv()` reads whatever data the client sends and echoes back using `conn.sendall()`.

__In the client side__
- We will simply do the following:
    - create a socket object
    - connect it to the server
    - send the message to the server using the method `sendall()`
    - use `recv()` method to read server's reply and print it.

#### Blocking Calls
> A socket function or method that temporarily suspends your application is a blocking call.
- `accept()`, `connect()`, `send()`, `recv()` are example of blocking method in python socket module. They don't return immediately.
- Blocking calls have to wait on the system calls (I/O) to complete before they can return a value.
- Blocking socket calls can be set to non-blocking mode so they can return immediately. Non-blocking mode is supported with `setblocking()`.
### Socket Programming.

> For [basic implementation](https://github.com/blac-siren/Build_X/tree/master/sockets/basic) the server will simply echo whatever it receives back to the client.
- The socket address family and protocal will use `socket.AF_INET(IPV4)`
- The port should be and integer from 1-65535 (0 is reserved)

    | Address Family  | Protocal      | Address tuple   |
    | ----------------|:-------------:| ---------------:|
    | __socket.AF_INET__| IPV4        | (host, port)    |
- `SOCK_STREAM` is the socket type for __TCP__, the protocal will use to transport our messages packets in the network.
- `accept()` [__blocks__](#blocking-calls) and waits for an incoming connection. When the client connects, it returns a pair (*conn*, *address*), where __conn__ is a new socket object usable to send and receive data on th connection, and the __address__ is the address bound to the socket on the other end of the connection.


A socket function or method that temporarily suspends your application is a blocking call. For example, accept(), connect(), send(), and recv() “block.” They don’t return immediately. Blocking calls have to wait on system calls (I/O) to complete before they can return a value. So you, the caller, are blocked until they’re done or a timeout or other error occurs.

Blocking socket calls can be set to non-blocking mode so they return immediately. If you do this, you’ll need to at least refactor or redesign your application to handle the socket operation when it’s ready.















Since the call returns immediately, data may not be ready. The callee is waiting on the network and hasn’t had time to complete its work. If this is the case, the current status is the errno value socket.EWOULDBLOCK. Non-blocking mode is supported with setblocking().















By default, sockets are always created in blocking mode. See Notes on socket timeouts for a description of the three modes.

Closing Connections
An interesting thing to note with TCP is it’s completely legal for the client or server to close their side of the connection while the other side remains open. This is referred to as a “half-open” connection. It’s the application’s decision whether or not this is desirable. In general, it’s not. In this state, the side that’s closed their end of the connection can no longer send data. They can only receive it.













I’m not advocating that you take this approach, but as an example, HTTP uses a header named “Connection” that’s used to standardize how applications should close or persist open connections. For details, see section 6.3 in RFC 7230, Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing.

When designing and writing your application and its application-layer protocol, it’s a good idea to go ahead and work out how you expect connections to be closed. Sometimes this is obvious and simple, or it’s something that can take some initial prototyping and testing. It depends on the application and how the message loop is processed with its expected data. Just make sure that sockets are always closed in a timely manner after they complete their work.




#### Blocking Calls
A socket function or method that temporarily suspends your application is a blocking call.
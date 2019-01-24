import sys
import selectors


class Message:
    def __init__(self, selector, sock, addrs):
        self.selectors = selector
        self.sock = sock
        self.addrs = addrs
        self._recv_buffer = b""
        self._send_buffer = b""
        self._jsonheader_len = None
        self.jsonheader = None
        self.request = None
        self.response_created = False

    def process_events(self, mask):
        if mask & selectors.EVENT_READ:
            self.read()
        if mask & selectors.EVENT_WRITE:
            self.write

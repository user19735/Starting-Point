import sys
import socket
import threading

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3 ) and chr(i) or '.' for i in range(256)]

    def hexdump(src, length = 16, show = True):
        if isinstance(src, bytes):
)

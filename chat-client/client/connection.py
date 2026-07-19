import socket

from config import (
    HOST,
    PORT
)


def create_connection(nickname):

    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    sock.connect(
        (HOST, PORT)
    )

    sock.sendall(
        (nickname + "\n").encode()
    )

    return sock
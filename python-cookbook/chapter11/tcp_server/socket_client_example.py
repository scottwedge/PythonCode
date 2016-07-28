#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM

def echo_client(sock, mesg):
    sock.send(mesg)
    return sock.recv(8192)

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 20000))
    print(echo_client(s, b'Hello'))

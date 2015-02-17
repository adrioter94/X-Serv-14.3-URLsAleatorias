#!/usr/bin/python

"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 7777))
mySocket.listen(5)


try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        x = random.randrange(10000)
        url = "http://" + socket.gethostname() + ":7777/" + str(x)
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hola. </h1>" +
                        "</p>" +
                        "<a href=" + url + ">Dame otra</a>"
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()

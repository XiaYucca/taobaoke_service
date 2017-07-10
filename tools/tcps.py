#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket


import SocketServer
from time import ctime

HOST = '192.168.1.69'
PORT = 5005
ADDR = (HOST, PORT)

def defaultList(d) :
    print d
    print "default listening "

listenFun = defaultList
data = ""


class MyRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        global listenFun
        print '...connected from:', self.client_address
        
        while True:
            global data
            data = self.request.recv(1024)
            self.request.sendall('[%s] %s' % (ctime(),data))

            if listenFun:
                print "run listenFun"
                listenFun(data)
#            print "%s"%(self.request.recv(1024))



def socketTest():
    TCP_IP = '192.168.1.69'
    TCP_PORT = 5005
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response
    
    print "start create socket servers ip: %s port: %d"%(TCP_IP,TCP_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        conn.send(data)  # echo
    conn.close()


def startServer():
    tcpServ = SocketServer.ThreadingTCPServer(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()

def addSocketListen(func):
    global listenFun
    listenFun = func


if __name__ == '__main__':
    tcpServ = SocketServer.ThreadingTCPServer(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()

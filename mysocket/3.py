import socket
import threading
import logging
import time
logging.basicConfig(level=logging.INFO)

class chatServer:
    def __init__(self):
        self.ipaddr = '192.168.1.1'
        self.port = 8080
        self.sock = socket.socket()

    def start(self):
        self.sock.bind((self.ipaddr,self.port))
        self.sock.listen()
        # threading.Thread(target=self.myaccept,name='start--thread').start()
        self.myaccept()

    def myaccept(self):
        while True:
            sock,client = self.sock.accept()
            threading.Thread(target=self.rev,args=(sock,)).start()
            # self.rev(sock)
    def rev(self,sock):
        while True:
            backinfo = sock.recv(1024)
            logging.info(backinfo)
            msg = b'hello test\n'
            sock.send(msg)

s = chatServer()
s.start()

while True:
    logging.info(threading.enumerate())
    time.sleep(3)
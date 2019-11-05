import logging
import threading
import socket
logging.basicConfig(level=logging.INFO)

class chatServer:
    def __init__(self,ip='192.168.1.1',port=9999):
        self.addr = (ip,port)
        self.sock = socket.socket()
        self.clients = {}

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        threading.Thread(target=self._accept,name='accept').start()

    def _accept(self):
        while True:
            sock, client = self.sock.accept()
            self.clients[client] = sock
            threading.Thread(target=self._recv,args=(sock,client)).start()
    def _recv(self,sock:socket.socket,client):
        while True:
            data = self._recv(1024)
            msg = data.decode()
            logging.info(msg)
            for s in self.clients.values():
                s.send(msg)
    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()

chat = chatServer()
chat.start()
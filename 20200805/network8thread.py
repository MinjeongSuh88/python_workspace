from socket import *
import threading
import time

ip = '192.168.0.68'
port = 5000

def send(sock):
    sendData = input('>>>')
    clientSock.send(sendData.encode('utf-8'))

def receive(sock)    :
    recvData = clientSock.recv(1024)
    print('서버가 보낸 메세지 :',recvData.decode('utf-8'))

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip,port))
print('접속 완료')

receiver = threading.Thread(target = receive, args = (clientSock,))
sender = threading.Thread(target = send, args = (clientSock,))

receiver.start()
sender.start()

while True:
    time.sleep(1)
    pass

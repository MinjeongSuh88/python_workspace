# 서버 사이드 함수 만들기 + Thread
from socket import *
import threading
import time

port = 5000

def send(sock):
    sendData = input('>>>')
    sock.send(sendData.encode('utf-8'))

def receive(sock):
    recvData = sock.recv(1024)    
    print('클라이언트 메세지 :',recvData.decode('utf-8'))

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)
print('%d반 포트로 접속 대기중'%port)

connectionSock, addr = serverSock.accept() # 클라이언트와 접속면 커넥션소켓과 ip어드레스를 리턴 받음
print(str(addr),'에서 접속되었습니다.')

# 수신용 쓰레드
sender = threading.Thread(target = send, args =(connectionSock,)) # 아규먼트는 튜플로 입력 받음

# 발신용 쓰레드
receiver = threading.Thread(target = receive, args =(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
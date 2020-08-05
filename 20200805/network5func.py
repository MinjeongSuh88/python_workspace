# 서버 사이드 함수 만들기
from socket import *
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

connectionSock, addr = serverSock.accept() # 클라이언트와 접속면 커넥션소켓과 어드레스를 리턴 받음
print(str(addr),'에서 접속되었습니다.')

while True:
    send(connectionSock)
    receive(connectionSock)
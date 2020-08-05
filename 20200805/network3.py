# 서버 사이드
# 계속 반복해서 듣기
from socket import *

port = 5000

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)
print('%d반 포트로 접속 대기중'%port)

connectionSock, addr = serverSock.accept() # 클라이언트와 접속면 커넥션소켓과 어드레스를 리턴 받음
print(str(addr),'에서 접속되었습니다.')

while True:
    recvData = connectionSock.recv(1024)
    print('클라이언트가 보낸메세지 :',recvData.decode('utf-8'))
    
    sendData = input('>>>')
    connectionSock.send(sendData.encode('utf-8'))


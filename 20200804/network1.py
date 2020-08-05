from socket import *
import random

serverSock = socket(AF_INET, SOCK_STREAM) # 소켓은 2개의 매개변수를 사용
# TCPIP
# 65535 ==> 8000-9000 port 개발용
serverSock.bind(('',5000)) # 5000번 포트를 사용
print('사용자의 접속을 대기합니다.')
serverSock.listen(1) # 연결 기다림(사용자의 요청 대기 중)
connectionSocket,addr = serverSock.accept() # addr :클라이언트의 ip주소
print(str(addr)+'연결 성공!')

data = connectionSocket.recv(1024) # 클라이언트로부터 받음
msg = data.decode('utf-8') # 클아이언트로부터 받은 data를 utf=8타입으로 재가공
print(msg)

response = ['왬마','왜불러','듣고있다','im listening','집에 언제 가지','배고프다']
connectionSocket.send(response[random.randint(0,len(response)-1)].encode('utf-8')) # 메아리 서버
print('서버 메세지 전송 완료')

# 클라이언트 사이드

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM) # 서버랑 연결해줘
# clientSock.connect(('127.0.0.1')) # LOOPBACK 어드레스, 내 랜카드에 갔다가 다시 돌아옴
clientSock.connect(('192.168.0.36',5000)) 
clientSock.send('yaho'.encode('utf-8')) # 서버에 전달, 네트워크는 패키 단위로 전달

data = clientSock.recv(1024)
print('서버가 보낸 데이터 :',data.decode('utf-8'))

print('연결 성공!!!')
from socket import *

ip = '192.168.0.36'
port = 5000

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip,port)) # 튜플 형식으로 써줘야 함
print('접속 완료')

while True:
    sendData = input('>>>')
    clientSock.send(sendData.encode('utf-8'))

    recvData = clientSock.recv(1024)
    print('서버가 보낸메세지 :',recvData.decode('utf-8'))
    



# 명령프롬프트) ping :물리적으로 접근이 가능한지 체크
# for i in range(1,65535): 
#     try :
#         clientSocket.connect(('183.111.159.83',i)) # 튜플 형식으로 써줘야 함, 포트는 랜덤으로
#     except:
#         print(i,'괜찮아.. 테스트잖아 힘내^.^')
# 포트 별로 사용하고 있는지, 에러 타입이 다름 -> 포트 스캔



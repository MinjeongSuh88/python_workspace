# 클라이언트 사이드
import socket
import threading

ip = '192.168.0.68'
ip = '192.168.0.5'
port = 5000

# 닉네임 결정
nickname = input('당신의 닉네임?')

# 서버에 연결
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((ip, port)) # 여기 ip로 연결하고 이 port를 사용

# 서버에 닉네임 전달
def receive(clientSock):
    while True:
        try:
            msg = clientSock.recv(1024).decode('utf-8') # 클라이언트소켓이 받은 것을 디코딩
            if msg == 'NICK':
                clientSock.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
    # 에러 발생 시 연결 끊기    
            print('에러 발생')
            clientSock.close()
            break

# 서버에 메세지 보내기
def send(clientSock):
    while True:
        msg = '{}: {}'.format(nickname, input(''))
        clientSock.send(msg.encode('utf-8'))

# 수신과 발신을 동시에 처리하기 위해 쓰레딩
receive_thread = threading.Thread(target = receive, args = (clientSock,))
receive_thread.start()

send_thread = threading.Thread(target = send, args = (clientSock,))
send_thread.start()




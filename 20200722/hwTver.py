# # 문제 1:세계 최최으 암호화 :알파벳을 3칸 미룸 a->d
# def setEncryption(a): # 함수가 실행될 때 받아온 인수를 a라는 매개변수에 넣음
#     v = ''
#     for i in range(len(a)):
#         code = ord(a[i])
#         code += 3
#         if code >= 91 and code <= 93:
#             code -= 26
#         elif code >= 123 and code <= 125:
#             code -= 26
#         v += chr(code)    
#     print(v)
#     return v
# setEncryption(input('영문 입력'))

# def getDecode(msg):
#     v = ''
#     for i in range(len(msg)):
#         code = ord(msg[i]) - 3
#         if 62 <= code <= 64 or 94 <= code <= 96: # 파이썬에서만 지원되는 기능
#             code += 26 
#         v += chr(code)    
#     return v 
# y=getDecode('ABCD')
# print(y)


# 문제 3
# 1) 컴퓨터가 세자리숫자를 생성한다
import random
com = []
while len(com) < 3: # for문으로 3번만 돌릴 경우 겹치는 랜덤넘버가 나오면 리스트가 2자리만 생성되는 경우도 있기 때문
    rnd = random.randint(0,9)
    if rnd in com:
        continue
    else:
        com.append(rnd)
print('컴퓨터 :',com)
# 6) 아니면 2번으로 돌아가서 반복한다
cnt = 0
while True:
    cnt += 1
    # 2) 사용자로부터 3자리숫자를 입력받는다
    userData = int(input('3자리 숫자를 입력하세요'))
    user = []
    user.append(userData // 100) # 3자리 숫자를 100으로 나눈 몫을 리스트 user에 담음 -> 100의 자리 숫자
    user.append(userData % 100 // 10) # 3자리 숫자를 100으로 나눈 나머지를 10으로 나눈 몫을 리스트 user에 담음 -> 10의 자리 숫자
    user.append(userData % 10)
    print(user)
    # 3) 판별한다
    strike=ball=0 # 랜덤 397, 사용자 307
    for i in range(3):
        if com[i] == user[i]:
            strike += 1  
        else:
            for j in range(3): # 이미 com과 user의 같은 자리의 요소르 비교하고 넘어왔기 때문에 반복되도 상관 없음
                if com[i] == user[j]:
                    ball += 1
    # 4) 출력한다
    print(str(strike)+'S',str(ball)+'B')
    # 5) 3strike이면 종료한다
    if strike == 3:
        print('짝짝짝 축하드립니다.',str(cnt)+'만에 성공하셨습니다.')
        break








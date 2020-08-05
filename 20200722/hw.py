# 문제 1:세계 최최으 암호화 :알파벳을 3칸 미룸 a->d
def setEncryption(str): 
    a = input('영문 입력')
    v = ''
    for i in range(len(a)):
        if ord(a[i]) >= 65 and ord(a[i]) < (90-2): # 대문자(65~90), 소문자(97~122)
            v += chr(ord(a[i])+3)
        elif ord(a[i]) >= (90-2) and ord(a[i]) <= 90:
            v += chr(ord(a[i])-23)
        elif ord(a[i]) >= 97 and ord(a[i]) < (122-2):
            v += chr(ord(a[i])+3)
        elif ord(a[i]) >= (122-2) and ord(a[i]) <= 122:
            v += chr(ord(a[i])-23)
    print(v)
    return v
setEncryption(str)

def getDecode(str):
    a = input('영문 입력') 
    v = ''
    for i in range(len(a)):
        if ord(a[i]) >= 65 and ord(a[i]) <= (65+2):
            v += chr(ord(a[i])+23)
        elif ord(a[i]) > (65+2) and ord(a[i]) <= 90:
            v += chr(ord(a[i])-3)
        elif ord(a[i]) >= 97 and ord(a[i]) <= (97+2):
            v += chr(ord(a[i])+23)
        elif ord(a[i]) > (97+2) and ord(a[i]) <= 122:
            v += chr(ord(a[i])-3)
    print(v)
    return v
getDecode(str)


# 문제 2
score=[[80,80,80,0,0],[60,50,80,0,0],[50,90,90,0,0],[40,50,60,0,0],[90,90,95,0,0],[85,95,100,0,0]]
for i in range(6):
    for j in range(3):
        score[i][3]+=score[i][j]
    score[i][4]=score[i][3]/3
print(score)    


# 문제 3
def BaseBall():
    import random
    r=str(random.randint(100,999))
    while True:
        u=(input('3자리 숫자를 입력하시오'))
        ball=0
        strike=0

        for i in range(3):
            if r[i] == u[i]: 
                strike+=1
        if r[0] == u[1] or r[0] == u[2]:
            ball+=1
        if r[1] == u[0] or r[1] == u[2]:
            ball+=1
        if r[2] == u[1] or r[2] == u[0]:
            ball+=1

        if strike == 3:
            print('입력 :',u,'\n'+'출력 : 정답 축하합니다. 성공하셨습니다.')
        else:
            print('입력 :',u,'\n'+'출력 : '+str(strike)+'S'+str(ball)+'B')
    
BaseBall()
            


# 문제 4
def printGuGuDan(x,y):
    for j in range(x,y+1):
        print(str(j)+'단')
        for i in range(1,10):
            print(j,'*',i,'=',j*i)

printGuGuDan(2,6)        

# 문제 1
for i in range(1,7):
    for j in range(1,7): # 주사위를 2개 돌려사
        if i + j == 4: # 합이 4면
            print('('+str(i)+','+str(j)+')') # 프린트


# 문제 2
y = int(input('연도입력:'))
if y % 4 == 0: # 4년 단위 중에
    if y % 100 != 0 or y % 400 == 0: # 100년 단위가 아니거나 400년 단위인 것 중에
        print(str(y)+'년은 윤년입니다.')
else:         
    print(str(y)+'년은 윤년이 아닙니다.')


# 문제 3
def hap(a,b):
    c=a+b
    return c
print(hap(100,200))
def minus(a,b):
    c=a-b
    return c
print(minus(200,100))
def multi(a,b):
    c=a*b
    return c
print(multi(200,3))
def div(a,b):
    c=a//b
    return c
print(div(200,3))


# 문제 4
li1=[[3,2,3],[4,5,6],[1,4,9]]
li2=[[1,8,7],[6,4,4],[3,2,3]]
for i in range(3):
    for j in range(3):
        li1[i][j]=li1[i][j]+li2[i][j]
        print(li1[i][j],end=',')
    print()


# 문제 5
for j in range(5):
    for i in range(1+5*j,6+5*j):
        li5=i
        print(li5,end=' ')    
    print()


# 문제 6
data=input('10명의 성적을 입력하시오').split()
print(data)
sum=0
for i in range(10):
    sum += int(data[i])
print('학생들의 총점 :',sum,', 학생들의 평균 :',sum/10)

    
# 문제 7
a=[]
a=list(range(1,101))
print(a)


# 문제 8
for i in range(100):
    if a[i] % 15 ==0:
        a[i]=3535
    elif a[i] % 3 == 0:
        a[i]=3333
    elif a[i] % 5 == 0:
        a[i]=5555
print(a)


# 문제 9
num=input('정수 10개를 입력하시오').split()
print(type(num[0]))
for i in range(10):
    if int(num[i]) % 3 ==0:
        print(num[i])
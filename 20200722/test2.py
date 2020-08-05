# 팩토리얼 함수 만들기 3!=6
def factorial(num): # 3!=3*2*1
    fac=1
    for i in range(num,0,-1):
        fac=fac*i
    print(str(num)+'! =',fac)
    return fac

x=factorial(3)
y=factorial(5)
print('x :',x,", y :",y,", x + y :",x+y)


# 팩토리얼 함수 만들기 3*2*1=6
def factorial2(num):
    '''이 부분은 도큐먼트 주석이라고 하는데 보통 함수에 대해 주석을 달기 위해 사용
    팩토리얼을 이와 같이 3 * 2 * 1 = 6 풀어서 프린트하는 함수
    '''    
    fac=1
    res=''
    for i in range(num,0,-1):
        fac=fac*i
        res+=str(i)+' * '
    print(res[:(num-1)*4+1],'=',fac)   
    return fac
factorial2(6)    
print(factorial2.__doc__)
help(factorial2)

def factorial3(num): # 선생님 버전
    fac=1
    for i in range(num,0,-1):
        fac=fac*i
        if i >= 2:
            print(i,'* ',end='')
        else:
            print(i,'=',fac,end='')
    return fac
factorial3(3) 

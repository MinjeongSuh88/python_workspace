# 내장함수
print(sum([10,20,30]), sum((10,20)), sum({2,3}))
print(bin(8)) #2진법
print(int(2.7), float(3), str(5)+'오')

a=10
b=eval('a+5') # eval :문자형으로 된 식을 실제로 계산할 수 있음
print(b)

print(round(1.2), round(1.6))

print('----------import-------------')
import math # import :수학과 관련된 함수들의 모듈을 불러오는 것
print(math.ceil(1.2), math.ceil(1.6)) # ceil :정수의 근사치 중 가장 큰 수
print(math.floor(1.2), math.floor(1.6)) # floor :정수의 근사치 중 가장 작은 수

print('--------------------')
bList=[True,1,False]
print(all(bList)) # all :True and 1 and False 를 모두 만족하냐?
print(any(bList)) # all :True or 1 or False 중 하나라도 만족하냐?


# 재귀적 호춣 :내가 나를 호출
print('--------------------')
def do1():
    print('첫번째 함수 실행 중')
def do2():
    print('두번째 함수 실행 중')
def do3(): # 함수가 다른 함수를 부를 수 있음
    print('세번째 함수 실행 중')
    do1()
    do2()
    print('세번째 함수 끝')
do3()    

def sayHello(cnt): # cnt라는 매개변수가 함수로부터 인자 5를 받아옴
    cnt -=1 # 함수가 실행되면 cnt는 4가 됨, 돌면서 1씩 작아짐
    print('hello~~~~')
    if cnt > 0: # cnt가 0이 되면 아래 행을 실행하지 않고 함수 종료
        sayHello(cnt) # 재귀적 호출은영원히.. 무한 루프에 빠지기 때문에 그만해야하는 조건을 지정해주어야 함
sayHello(5)    

# 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1) # 팩토리얼 함수를 처리하다가 중단하고 다른 팩토리얼 함수를 열어서 n-1를 실행, 그것을 반복, n이 1이 될 때 마지막 함수값을 리턴 리턴 리턴...
print(factorial(5))

# 피보나치 수열
def fibona(n):
    if n<= 1: # n이 2일 땐 인수가 각 1과 0인 피보나 함수가 실행되어야 하는데 해당 조건에 의하여 두 결과는 각각 1과 0이므로 결국, 인수가 2인 피보나 함수 결과는 1이다.
        return n
    return fibona(n-1)+fibona(n-2)
print(fibona(1))
print(fibona(2))
print(fibona(3))
print(fibona(4))
print(fibona(5))
print(fibona(6))
print(fibona(7))
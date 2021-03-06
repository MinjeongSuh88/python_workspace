# 중첩 함수 :함수 안에 다른 함수을 정의
def sayHello(): 
    msg='찌누'
    def prt():
        print(msg) # 내부 함수는 외부 함수의 변수를 가져다 쓸 수 있음(읽기전용 개념이기 때문에 수정은 안 됨)
    prt() # 함수의 바깥에서는 내부 함수를 알 수 없으므로 외부 함수가 실행해야줘야 함

sayHello() # 함수의 외부에서는 내부 함수를 알 수 없음


print('--------------------------------')
def f1():
    a=10 # f1 함수의 지역변수
    def f2(): # f1 안에 있는 중복 함수 
        a=20 # f2함수의 지역변수
    f2()
    print(a) # f2가 실행된후 f2의 지역 변수 a는 사라짐

f1() # 함수 f2가 실행 후 f2의 지역 변수 a는 사라지기 때문에 f1의 지역 변수가 프린트 됨


print('-----------nonlocal------------')
def f1():
    a=10 # f1 함수의 지역변수
    def f2(): # f1 안에 있는 중복 함수 
        nonlocal a # 나 바로 밖에 있는 함수의 지역 변수 a를 사용
        a=20 # f2함수의 지역변수
    f2()
    print(a) 

f1()    
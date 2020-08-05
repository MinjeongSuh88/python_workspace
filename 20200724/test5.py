# 함수를 호출할 때 다시 꺼내서 사용하는 함수 :클로저(closure)
def plus_ten(): 
    a = 10 # 지역 변수 ->원래 함수가 실행되면 메모리에서 사라져야 하는데 리턴된 add함수가 사용해야하기 때문에 메모리에 계속 남아 있음
    def add(b): # 중첩 함수
        return a+b # plus_ten의 지역 변수 a사용
    return add # 반환값으로 함수를 사용

cal = plus_ten() # cal = add ->함수 실행하여 리턴된 값(함수 add)을 변수 cal에 담음 
print(cal(1))


print('---------람다로 표현----------')
def plus_ten2():
    a = 10 # a라는 값을 외부에 노출하고 싶지 않을 때 사용하는 방법
    return lambda b: a+b # 위 3줄을 한 줄로 요약

cal2 = plus_ten2()    
print(cal2(100), cal2(200))
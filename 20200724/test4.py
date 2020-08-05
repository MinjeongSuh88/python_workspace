# 파이썬의 함수는 모두 일급 함수
# 함수를 다른 함수의 인수로 전달 가능
# 반환값으로 함수를 사용 가능
# 변수에 저장할 수 있음
def add(a,b):
    return a+b

# print(add(100,200))
plus=add # 함수를 다른 변수에 저장
print(plus(500,400))

def appendFunction(f1,c,d): # 이 함수에 매개 변수 3개 적용
    return f1(c,d) 

print(appendFunction(add,1000,2000)) # -> 리턴값이 add(1000,2000) :add함수를 다른 함수의 인수로 전달
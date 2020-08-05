# 리스트 내포 표현식 List Comprehension
# : 리스트 내부에 반복/조건문의 축약형 형태 전달 가능
# [리턴값 for i in 대상]
# [리턴값 for i in 대상 if 조건]
mlist=[1000,2000,3000,4000,5000] # 만원
# for i in range(len(mlist)):
#     mlist[i] = int(mlist[i] * 1.1)
# print(mlist)
print([int(i * 1.1) for i in mlist]) 


# 1월 어느날 최고 온도
# 영상인 날짜의 온도만 리스트로 작성하려고 한다.
list2 = [-5,-2,-1,0,2,-3,-2,10,3]
# list22 = []
# for i in range(len(list2)): # for문 버전
#     if list2[i] > 0:
#         list22.append(list2[i])
# print(list22)        
print([i for i in list2 if i > 0]) # 리스트 내포 표현식 버전


# Garbage Collector가 상주하고 있음
print('----------람다------------')
# 람다함수(익명함수-이름이 없는 함수):메모리를 절약하고 코드를 간겷하게 하기 위해, 1회용 함수
# def test(x):
#     return x+1
# print(test(100))    
print((lambda x: x+1)(100)) # 원래 함수가 있어야할 자리에 괄호로 묶은 람다함수를 그대로 대입
print(lambda x: x+1(100)) # 원래 함수가 있어야할 자리에 괄호로 묶은 람다함수를 그대로 대입

print('--------람다 합--------')
print((lambda a,b: a+b)(100,200)) 
def plusData(a,b):
    return a+b
c=100
d=200
print(plusData(c,d))

print(type(plusData),id(plusData)) # 파이썬은 함수도 일종의 객체(메모리를 할당하고 있음)
pd=plusData # pd라는 함수에 plusData 함수의 주소를 복사함
print(id(plusData),id(pd))
print(pd(500,200))

lmadd=lambda a,b: a+b # 익명 함수 주소를 lmadd 함수에 복사함
print(lmadd(1000,2000))

print('-------조건식을 사용한 람다---------')
print((lambda a,b: a if a%2==0 else b)(100,31)) # 두 개의 매개변수 중에서 짝수를 출력하는 익명함수





# print('--------람다 자리 바꿈---------')
# # 자리바꿈 해주는 함수
# def changeData(a,b):
#     a,b=b,a
#     return a,b
# c=100
# d=200
# c,d=changeData(c,d)    
# print('c :',c,', d:',d)

# print((lambda a,b: a=b,b=a)(100,200))





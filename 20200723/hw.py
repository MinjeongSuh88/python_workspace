print('------문제 1-------')
# 영문/숫자 가능, 영문 대소문자 구분, 특수문자 불가, 첫 글자로 _외에 영문만 가능


print('------문제 2-------')
def square(n):
    return n**2 
print(square(5))


print('------문제 3-------')
print((lambda n: n**2)(5))


print('------문제 4-------')
m=list(range(1,101))
def triple(n):
    return n*3      
print(list(map(triple,m)))


print('------문제 5-------')
print(list(map((lambda n: n*3),m)))


print('------문제 6-------')
rnd=[]
import random
def rn(n):
    while n > 0:
        if random.randint(1,100) in rnd:
            continue
        else:
            rnd.append(random.randint(1,100))
            n -= 1
    return rnd, max(rnd), min(rnd)
print(rn(10))


print('------문제 7---------')
k=[]
for i in range(1,101):
    k.append(i)
print(k)


print('--------문제 8-------')
print([i for i in range(1,101)])


print('--------문제 9--------')
print([i for i in range(1,101) if i%2 ==0])
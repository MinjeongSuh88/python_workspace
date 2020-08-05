def add(x,y):
    '''두 수의 합을 리턴합니다.'''  
    print(x+y)
    return x+y

def minus(x,y):
    '''두 수의 차를 리턴합니다.'''
    print(x-y)
    return x-y
     
x=add(100,200)
y=minus(200,100)
print(x+y)
help(add) # 두 수의 합을 리턴
help(minus) # 두 수의 마이너스를 리턴


def add_minus(a,b):
    return a+b,a-b # 함수의 리턴값은 정수, 문자, 실수, 튜플, 리스트... 다 가능
x,y=add_minus(300,200) # 동시에 2개의 값을 리턴하여 각 변수에 담을 수 있다
print("x :",x,", y :",y)

i,j=(1,2) # 언패킹 :튜플을 각 변수에 담는 것
i,j=1,2 # 괄호를 안 써도 튜플임
i,j=[1,2]


print('-------------------')
def hap(x,*y): #  y는 가변인수
    print('x :',x)
    print('y :',y) 
    return  x,y
hap(100,200) 
hap(100,200,300) # 가변인수 y는 튜플로 반환

# for k in (100,200):
#     v += k
# print(v)    
def hap2(x,*y): 
    '''x, y의 누적합 구하기'''
    v = x
    for k in y:
        v += k
    print('x :',x)
    print('y :',y)
    return v
print(hap2(100,200))
print(hap2(100,200,300))

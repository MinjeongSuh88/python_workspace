# 숫자형 변수
# 정수형(integer) ==>int
# 실수형(float) 3.14 ==>float()
# 복소수(complex) 1.3+1.9j # 원래는 i인데 전산에서는 i라는 변수를 많이 씀으로 j로 대체해서 사용

# 동적타이핑 언어 : 자료형을 미리 지정하지 않고 할당하는 순간 결정
a=10
print(type(a)) # 변수 a의 값의 타입을 출력

b=3.14
print(type(b)) # 변수 b의 값의 타입을 출력

b=20 # 한 번에 한 개만 기억할 수 있기 때문에 기존에 담겨있던 값 3.14는 지워짐
print(type(b),b) # 위에서는 자료형이 float이였지만 여기에서는 int으로 바뀜

c="10"
print(type(c))
# 형변환 : int(), float(), complex(), str()
print("a: "+a) # str() :변수a를 문자형으로 변환하면 연결연산자 사용 가능
print("b:",b)
print("c:"+c) # 문자끼리에서는 +가 연결연산자로 사용됨


a=10
b=20
print("before-a:",a,"b:",b)
temp=a
a=b
b=temp
print("after-a:",a,"b:",b)

a,b=b,a
print("=====> a:",a,"b:",b) # 파이썬에서는 임시 변수가 필요 없음

x=10
y=10
z=10
print("x:",x,"y:",y,"z:",z)
x=y=z=20
print("x:",x,"y:",y,"z:",z) # 여러 변수에 한 번에 값을 할당할 수 있음

i,j=100,200
print("i:",i,"j:",j)

# 아무 것도 없는 값
x=None # 다른 언어들은 null
print(x)

a=100 # a변수에 100을 할당
a+=20 #a=a+20과 같은 의미
print(a) # a변수에 20을 증가시킨 후 출력



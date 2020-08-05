# 튜플 :list와 유사, 읽기 전용

t='a','b','c','d' # 괄호 안에 넣는 것이 원칙이지만 괄호 없이도 가능
print(t,type(t))

t2='a','b','c','d' 
print(t2,type(t2))
print(t2,len(t2)) # 요소의 개수
print(t2.count('a')) # 글자의 개수
print(t2.index('b')) # index 번호

x=(1,2,3)
# x[0]=10 :튜플은 읽기 전용이기 때문에 요소의 수정이 불가
print(x) 

x2=(3) # 괄호 안에 그냥 값 1개만 있으면 튜플로 인식 안 함
x3=(3,) # ,를 포함하여 튜플로 인식
print(x2,type(x2)) 
print(x3,type(x3))

print("x :",x)
y=list(x) # 리스트로 형변환 하기
y[2]=30 # 바뀐 리스트에서 요소 수정
print(y)
x=tuple(y) # 다시 튜플로 형변환
print('x :',x)

t1=(10,20)
t2=list(t1) # 튜플 t을 리스트로 바꿔 t2에 저장
t2[0],t2[1]=t2[1],t2[0] # 리스트 t2의 요소 0번째와 1번째의 값 서로 바꿈
t1=tuple(t2) # 리스트 t2를 튜플로 바꿔 t1에 다시 저장
print(t1)

t1=(10,20)
a,b=t1
a,b=b,a
t1=(a,b)
print(t1)
print("----------------")
t1=(10,20)
t2=list(t1)
t2.reverse()
print(t2)
print(tuple(t2))




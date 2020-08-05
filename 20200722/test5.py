# 똑같은 값을 가져와서 사용할 때 reference(변수가 가지고 있는 값의 주소)가 같음 ->메모리 공간을 줄이기 위해
# 객체 :mutable, immutable
# mujtable(잘 변하는) :list, set
# immutable(잘 안 변하는) :bool, int, float, tuple. str
a = 100 # 100의 참조주소를 a가 가지는 것
b = a # 100에 담긴 값의 참조주소를 b가 가지는 것
print(type(a),type(b))
print(id(a),id(b)) # 결국 a와 b의 참조주소는 같게 됨

a = a + 1 #  a에 새로운 값의 참조주소를 넣음
print(id(a),id(b)) # 변수 a와 b의 참조값이 달라짐


print('------------list-------------')
m = [1,2,3]
n = m
print(id(m),id(n)) # 리스트 m과 n의 참조값은 같음

print(n[0])
n[0] = 500 # 리스트 m과 n의 참조값은 같기 때문에 m[0]의 값도 달라짐 ->이런 위험을 
print('m[0] :',m[0],', n[0] :',n[0])
print('id(m) :',id(m),', id(n) :',id(n))


print('-----내용만 카피해서 다른 주소 설정-----')
k = m[:]
print(id(m),id(k)) # 리스트 m과 슬라이스 k의 참조값이 다름
k[0] = 100
print('m[0] :',m[0],', k[0] :',k[0]) # 다른 주소이기 때문에 리스트 k의 [0]요소만 바뀜
print('id(m) :',id(m),', id(k) :',id(k))

c = [10,20,30]
d = c[:]
print(id(c),id(d)) # 리스트 m과 슬라이스 k의 참조값이 다름
print(c == d) # 그러나 내용은 같음
print(c is d) # c와 d가 같아?


print('----mutable 안의 mutable 의 참조 확인 ----')
q = [[1,2],[3,4]]
p = q[:]
print(id(q),id(p)) # 서로 다른 참조
print(id(q[0]),id(p[0])) # 내부 객체는 같은 참조
p[0][0] = 5
print(q[0][0],p[0][0]) # 서로 다른 참조
print(id(q),id(p)) # 서로 다른 참조
print(id(q[0]),id(p[0])) # 내부 객체는 같은 참조


# shallow copy :표면적으로 주소만 복사하는 것
# deep copy :자손의 자손까지 아예 다르게 카피
import copy
s = [[1,2],[3,4]]
t = copy.deepcopy(s)
print('id(s) :',id(s),', id(t) :',id(t))
print('id(s[0]) :',id(s[0]),', id(t[0]) :',id(t[0]))

s[0][0] = 300
print('s[0][0] :',s[0][0],', t[0][0] :',t[0][0])
print('id(s) :',id(s),', id(t) :',id(t))
print('id(s[0]) :',id(s[0]),', id(t[0]) :',id(t[0]))

# set: 순서 x, 중복 x
a={1,2,3,4}
print(a,type(a))
# print(a{0})  순서가 없어서 몇 번째의 값을 뽑아올 수 없음
b={3,4}
print(a.union(b)) # .union :합집합(|)
print(a.intersection(b)) # .intersection :교집합(&)
print(a-b,a|b,a&b) 

b.add(5,6)
print(b)

b.update({6,7})
print(b)

b.update((8,9)) # 튜플 추가 가능
print(b)

b.update([10,11]) # 리스트 추가 가능
print(b)

b.discard(7) # 제거
print(b)

b.remove(8) # 폐기
print(b)

print("----------------------")
c=set()
c=b
print(c)
c.clear() # 요소들 모두 삭제
print(c)

# 다음 리스트의 중복된 값을 제거
m=[2,3,11,29,3,2,7,8,11]
m=set(m) # set 으로 형변환하면 중복이 사라짐
print(m)
m=list(m) # 다시 리스트로 변환
print(m)



# 리스트 :순서 O, 중복 O, 변경 O

a=[1,2,3]
print(a,type(a))

b=[10,a,True,'문자열']
print(b[1])
print(b[1][2]) # 리스트 b의 1번째의 2번째

c=[[1,2],[3,4,5],[6,7,8,9]]
print(c)
print(c[2][2])

pet=['강아지','고양이','거북이','고슴도치']
print(pet)
pet.append('열대어') # 리스트에 끝에 추가, 1개만 사용
print(pet)
pet.remove('거북이') # 리스트에서 삭제, 1개만 사용
print(pet)
pet.insert(0,'이구아나') # 리스트 내 위치 정하여 삽입
print(pet)
pet.extend(['토끼','햄스터']) # 한 번에 확장하여 끝에 삽입
print(pet)

pet+=['돼지'] # 연산자로도 삽입 가능
print(pet)
print(len(pet))
del pet[3] # 몇 번째 위치로도 삭제 가능
print(pet)  

animal=pet
print('animal :',animal)
print('pet :',pet)

pet[0]='멍멍이'
print('---------------')
print('animal :',animal) # 리스트 pet의 요소로 수정했더니 animal에도 바뀜
print('pet :',pet)
print(id(animal),id(pet)) # 그 이유는 같은 대상(이름만 다름)을 참조

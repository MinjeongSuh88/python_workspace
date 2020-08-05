# dict :딕셔너리, 키:값의 쌍으로 이루어짐, 순서 x

mydic=dict(k1=1,k2='abc',k3=3.4) # 값은 정수, 실수, 문자형 아무거나 상관없음
print(mydic)

dic={'파이썬':'뱀','자바':'커피','오라클':'예언자'} # 키:값 쌍을 이룸
print(dic,len(dic))
print(dic['자바']) # 인덱스가 아니랴 키값으로 값을 뽑아냄

dic['스미스']='백그라운드프로세스' # 새로운 키:값을 추가함
print(dic)

dic['neo']='주인공'
dic['스미스']='bg' # 있던 키를 사용하면 값을 덮어씌움
print(dic)

for key in dic: # 키만 출력
    print(key)

for val in dic.values(): # 밸류값만 출력
    print(val)

for key, val in dic.items(): # 딕셔너리에서 키와 밸류값을 각각 꺼내줌
    # print('key = '+key+', value = '+val)
    print('key = {key}, value = {val}'.format(key=key, val=val)) # 문자열 안에 변수처럼 사용할 수 있음

print('neo' in dic) # in :키가 있는지 여부 판단
del dic['neo'] # 키 값이 neo인 항목삭제

# dic.clear() # 초기화되어 사라짐
print(dic)
# json : 원래는 자바스크립트에서 갹채룰 표시하는 표기법
# 서로 다른 곳에서 데이터 교환 방식으로 사용되기 시작함, 파이썬과 연결할 때 딕셔녀리를 주로 사용


print("----------------------------")
dic['game']=['대항해시대','바람의나라','문명6','토탈워'] # 딕셔너리에 밸류값을 리스트, 튜플 등으로 입력 가능
print(dic)

dic['broadcasting_co']=['kbs','mbc','sbs','ytn','jtbc']
print(dic)

from pprint import pprint as pp # 줄 맞추기
pp(dic)

fruit={'귤':'제주도','포도':'카프카','딸기':'서울','망고':['대구','필리핀']}
print(fruit['딸기'])
print(fruit['망고'])
for key, val in fruit.items():
    print(key, val)


        



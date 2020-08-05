print('-------문제 1--------')
# lambda x: return x+10


print('-------문제 2--------')
cnt="Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO!".split()
print([len(i) for i in cnt])


print('-------문제 3--------')
print([i for i in cnt if len(i) >= 4])


print('-------문제 4--------')
do_city  = { "경기도":"수원", "강원도":"춘천"}
print({key:val for key,val in do_city.items()})


print('-------문제 5--------')
# 지역 변수는 자신이 정의된 구역(함수) 내에서만 존재하므로 함수가 실행되면 메모리에서 사라짐
# 전역 변수는 전체에 존재


print('-------문제 6--------')
# show()는 함수 show의 지역 변수인 a의 값 200을 출력
# print(a)는 전역 변수인 a의 값 100을 출력


print('-------문제 7--------')
# global a


print('-------문제 8--------')
# print(locals())


print('-------문제 9--------')
# 500


print('-------문제 10--------')
# nonlocal data1
  

print('-------문제 11--------')
# 1. 함수를 다른 함수의 매개변수로 사용 가능
# 2. 함수를 리턴값으로 사용 갸능
# 3. 함수를 다른 변수에 저장 가능


print('-------문제 12--------')
# 1100


print('-------문제 13--------')
# 클로저


print('-------문제 14--------')
# 정규 분포식


print('-------문제 15--------')
# 1. regular 모듈을 import
# 2. 컴파일에 패턴을 지정
# 3. 조건에 맞는 문자열을 match/search/findall/finditer 중 하나 선택하여 실행


print('-------문제 16--------')
t="Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 ".split()
print([i for i in t if i.find('-') != -1])


print('-------문제 17--------')
import re
c=re.compile('[0-9]{3}-[0-9]{4}-[0-9]{4}')
print(c.search("Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 ").group())

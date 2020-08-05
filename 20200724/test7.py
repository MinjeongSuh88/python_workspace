import re
p = re.compile('[a-z]+') # compile 안에 패턴을 만들어 줌, 패턴 :정규식을 컴파일한 결과
print(p,type(p)) # 패턴과 패턴의 타입을 출력

# 문자열 검색
# match() :문자열의 처음부터 시작하여 정규식와 매치되는지 조사하여 처음 만나는 것
# search() :문자열 전체를 검색하여 정규색과 매치되는지 조사
# findall() :정규식과 매치되는 모든 문자열을 리스트로 돌려줌
# finditer() :정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려줌
m = p.match('regular expression') # 문자열이 패턴 p와 매칭되는지 조사하여 첫번째열부터 끝나는 깞까지를 변수 m에 담음
print(m) # <re.Match object; span=(0, 7), match='regular'> :

if m: # 만약 문자열이 패턴 p와 매칭되면
    print(m.group()) # 값을 출력
else: # 아니면
    print('no match') # no match라는 문자열 출력


print('----------------')
result = p.match('9999999 aaaaabbbbbb') # 문자열 안에 패턴과 매칭되는 첫글자가 없으면 끝
print(result) # 그래서 None이 프린트 됨

result2 = p.findall('hello python world today is monday') # 문자열 안에 패턴과 매칭되는 것들을 리스트로 모두 가져옴
print(result2) # ['hello', 'python', 'world', 'today', 'is', 'monday']

# for문으로 1개씩 출력
for i in result2: # 리스트 result2에 담겨있는 요소들을 한 개씩 출력
    print(i)

print('----------------')
result3 = p.finditer('today is monday') # 문자열을 반복할 수 있는 객체로 가져와서 변수 result3에 담음
print(result3) # <callable_iterator object at 0x03900FB8> :값이 iterable객체로 담겨있음 보여줌
for data in result3:
    print(data) # <re.Match object; span=(0, 5), match='today'> :match한 각 객체의 정보
    print(data.group()) # group :객체의 값을 보여줌
    print(data.start(),':',data.end()) # start :객체의 시작 정보, end :객체의 끝 정보


print('-----------------')
msg = '999,999 smartphone bbb@naver.com aaa@gmail.com'    
# 이메일만 선택해서 출력
p1 = re.compile('[a-zA-Z0-9.]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+')  # 패턴을 정함
email = p1.findall(msg) # 패턴 p1과 매치되는 모든 문자열을 리스트로 돌려줌
for i in email: # 리스트 email에서 요소 하나씩 빼서 프린트
    print(i)
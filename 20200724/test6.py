# 정규 표현식(Regular Expression)``
# 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
# 대부분의 텍슽 편집기와 프로그램언어에서 문자열의 검색과 치환을 위해 지원함
msg='aaa bbb 필라테스 힘들어 육체노동 eee smith@naver.com 010-1234-5678 aaa@gmail.com'
email=msg.split()
print([m for m in email if m.find('@') != -1]) # 문자열에서 이메일주소만 추출
# DNS -> .Root

import re # regular
# re.match('패턴','문자열')
print(re.match('Hello','Hello Python World'))

# 문자열.find()
print('Hello Python World'.find('Hello'))

# 첫글자가 H로 시작? ^H
print(re.match('^H','Hello Python World'))

# 끝글자 :d$
print(re.search('ld$','Hello Python World'))

# 010-1234-5678
print(re.match('[0-9]+','1234')) # + :숫자가 1개 이상
print(re.match('[0-9]*','1234')) # * :숫자가 0개 이상

# aaabbbb
print(re.match('a+','aaabbbb')) # a가 1개 이상 잇나?
print(re.match('a+b','aaabbbb')) # a가 1개 이상, b 1개 잇나?

print(re.match('[가-힣]','불금달료보자.'))

# ab9cd, ab9999cd
print(re.match('ab[0-9]?cd','ab9cd')) # ? :0 or 1
print(re.match('ab[0-9]?cd','ab9999cd'))
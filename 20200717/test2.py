# 자료형

s='sequence'
print(s, len(s), s.count('s'), s.find('e')) # .count :개수 셈, .find : e의 위치 찾음
print(s.find('e',2,6)) # 2번째부터 6번째 사이에서 e를 찾음, 
print(s.find('e',3), s.rfind('e')) # 끝을 안 쓰면 시작점 3번째부터 끝까지에서 e 찾음, 오른쪽에 있는 e를 찾음
print(s.find('e',5,7)) # 못 찾으면 -1로 출력

ss='mbc'
print('mbc',type(ss),id(ss)) # id는 변수의 위치, 주소
print(s,s[2:4],s[:3],s[3:],s[3::2]) # 슬라이싱 :qu,seq,uence,une

msg="   Hello  Python "
print(msg)
print(msg.strip()) # strip() :좌,우 공백없이 출력 -> 사용자들의 입력값으로부터 공백을 없앨 때 주로 사용
print(msg.rstrip()+"^^") # rstrip() :오른쪽만 공백없이
print(msg.lstrip()+"^^") # rstrip() :왼쪽만 공백없이

msg="구정,신정,크리스마스,초파일,추석"
m=msg.split(',') # 변수 msg에 담긴 문자열을 콤마 단위로 리스트 m에 대입
for i in m: # 반복문 시작 :리스트 m에 담긴 i
    print(i)

msg3=list('hello')
print(msg3)
str_time=['10','44','30']
print(":".join(str_time)) #" ".join() :괄호 안의 리스트 요소 사이 사이에 문자열을 추가해서 문장열

print(msg3[4])
msg3[0]='m'
print(msg3)


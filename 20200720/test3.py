# 사용자로부터 입력 받은 값이 대문자인지 소문자인지 구분
data=input("영문 한 글자를 입력하시오")
print(data) 
print(ord(data)) # 이 값의 아스키코드 값을 구함(A=65, a=97)
if ord(data) >= 65 and ord(data) <= 90: # 판단 후 출력-대문자(65~90), 소문자(97~122)
    print(data+"는 대문자 입니다. 아스키코드는", ord(data)) 
elif ord(data) >= 97 and ord(data) <= 122:
    print(data+"는 소문자 입니다. 아스키코드는", ord(data))

    

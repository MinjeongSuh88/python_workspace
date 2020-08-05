# 글자를 소문자로 변환
msg='hELLo'
print(len(msg))
for i in range(5):
    # print(msg[i])
    code=ord(msg[i]) # 각 글자의 아스키 코드값 구함
    if code >= 65 and code <= 90: # 대문자라면 이것을 아스키코드를 사용하여 소문자로 바꿔줌
        print(chr(code+32), end='') # 아스키코드를 문자로 변환하여 출력
    elif code >= 97 and code <= 122:
        print(chr(code-32), end='') 
print()

# 사용자로부터 받은 값을 대소문자를 변경        
msg1=input("영문을 입력하시오")
print()
for i in range(len(msg1)):
    # print(msg[i])
    code=ord(msg1[i]) # 각 글자의 아스키 코드값 구함
    if code >= 65 and code <= 90: # 대문자라면 이것을 아스키코드를 사용하여 소문자로 바꿔줌
        print(chr(code+32), end='') # 아스키코드를 문자로 변환하여 출력
    elif code >= 97 and code <= 122:
        print(chr(code-32), end='') 
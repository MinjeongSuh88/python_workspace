while True: # 무한 반복
    value=int(input('숫자를 입력하세요'))
    if value % 5 == 0:
        print(str(value)+'는 5의 배수 입니다.')
        continue # 아래에 있는 명령어를 실행하지 않고 다시 위로 올라감(오늘은 여기까지?)
    else:
        print(str(value)+'는 5의 배수가 아닙니다.')
print("이제 그만......")
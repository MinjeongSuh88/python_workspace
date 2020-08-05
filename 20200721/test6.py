import random
i=random.randint(1,100)
while True:
    u=int(input('1부터 100 사이의 숫자 하나를 입력하시오'))
    if i == u:
        print("두 수가 일치합니다.")
        break
    else:
        if i > u:
            print("더 올려봐~")
        else:
            print("내려..")
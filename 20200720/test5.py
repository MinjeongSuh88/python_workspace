# 사용자로부터 숫자를 입력받아 홀수인지 짝수인지 판단
num=int(input("숫자를 입력하시오"))
if num%2 == 0:
    print(num,"은 짝수입니다.")
elif num %2 != 0:
    print(num,"은 홀수입니다.")

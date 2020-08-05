# 예외 :프로그램 실행 중 발생한 예상치 못한 오류(가벼운 오류)
# 예외는 처리해줄 수 있음 case by case

# try:  -> 예외가 발생할 수 잇는 지역
#   문장 1
#   문장 2
# except 예외로 인한 에러:
#   예외처리문장1
#   예외처리문장2
class EvenError(Exception): # 사용자 정의형 예외, 부모 클래스 Exception를 상속받은 EvenError
    def __init__(self,msg):
        self.msg = msg

    def __str__(self): # 매직 함수
        return self.msg

a = EvenError('d') 
print(str(a))

from random import randint
try:
    n = int(input('숫자 입력 :'))  
    if n % 2 == 0: 
        raise EvenError('홀수만 입력해라.. ^.^') # msg매개변수에 해당 문자열이 대입
    for i in range(10): # 랜덤값이 0이 나올 수 있을 경우의 수 대로 상황 반복
        a = randint(0,9)    
        print(n/a)
except EvenError as ee: # 원래 아니였던 걸 사용자 임의로 에러 케이스를 추가함
    print(ee) # 에러 문구 출력
    print('짝수는 안 해줘')
except ValueError:
    print('숫자만 입력해')        
except ZeroDivisionError:
    print('0으로 나눌 수 없음') 
finally:
    print('이 부분은 예외가 있던 없던 항상 실행됩니다.')

# 에러


# 연관된 함수들의 모음 :모듈
# salary라는 모듈 안에 raise_sal, reduce_sal이라는 함수 정의해놓음

author='서민정' # 작성자 이름 기록

def raise_sal(sal): # 급여를 전달하면 10% 인상된 급여를 리턴
# '''나중에는 데이터베이스를 연결해서 누구의 급여를 인상하는 것 할 수 있음'''
    return int(sal*1.1)

def reduce_sal(sal): # 20% 감소, 소수점 없이 함수
    return int(sal*0.8)

# test code
if __name__ == '__main__': # 이름이 메인일 때만 실행하는 조건 -> 다른 파일에서는 아래의 코드 실행 안 됨
    print(raise_sal(3000)) # 함수를 실행할 때 매개변수에 3000을 대입 -> 리턴값으로 대체되어 출력
    # 3300.0000000000005 ->2진수로 실수를 표시할 때의 연산 상의 오차로 인한 소수점 발생
    print(reduce_sal(1000))

    print('잘 나오나?',author)
    
    print(__name__) # 모듈의 이름을 출력

    
# __name__ :모듈의 이름을 가진 변수
# print(__name__) :다른 파일에서 실행하면 이 파일의 이름 salary가 출력됨
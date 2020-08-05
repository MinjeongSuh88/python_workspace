# fuction :함수
# 반복되는 코드를 줄여주기 위해 특정 코드에 이름을 부여해놓은 것
# 내장함수

# 불러서 실행 :호출
# def 함수명(매개변수, 매개변수, ..)
#   실행문장
#   실행문장
#   return 결과값
print('1111111111111111111')
def double(x):
    print('22222222222222222') # print('22')는 함수 사이에 껴있기 때문에 함수 실행 후 프린트됨, 33보다 뒤에 실행
    return x*2 # 이것의 결과값을 날 불러준 애에게 돌려줘 -> 반환
print('33333333333333') 

y=double(10) # 10 :전달하는 값 -> argument(인수) 
print(y)

k=double(20)
print(k)


print('-------------------') # 로또 번호 생성기
def getLotto(num):
    for i in range(num):
        lotto=[]
        import random # 랜덤하게 1부터 45사이의 정수 생성
        i = 0
        while i < 6: # 6자리가 모두 완성되면
            r = random.randint(1,45)
            if r in lotto: # 중복된 값이 있으면 다시 뽑음
                continue
            else:
                lotto.append(r) # lotto 리스트에 담음
                i += 1
        lotto.sort() # 정렬 
        print(lotto) # 출력
    
getLotto(5)



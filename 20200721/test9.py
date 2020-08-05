# 함수 :여러개의 실행문을 하나의 묶음으로 만든 실행단위
# 내장함수 : 설치 후에 포함되어 있는 함수
# 사용자정의함수 :

for i in range(1,6):
    print('*'*i)
print('-------------------------------')
for j in range(1,6): # 2중 for문으로 작성
    for i in range(j):
        print('*',end='')
    print()
print('-------------------------------')

# def 함수명()
#     문장
#     문장
#     [return 반환값]
def printStar(): # 함수 정의
    num=10 # 값이 10인 함수 정의
    for i in range(1,num): # i의 범위가 1부터 num 전까지
        print('*'*i)
printStar() # 함수를 만나면 위에 있는 함수코드를 실행하고 다시 돌아옴 
printStar() # 함수를 몇 번 실행했는지 눈으로 보기 쉬움

def printStar1(num): # 함수를 실행할 때 num라는 매개변수를 활용하겠다는 의미
    for i in range(1,num):
        print('*'*i)
printStar1(5) # 함수를 실행할 때 num에 5를 대입
printStar1(7) # 함수를 몇 번 실행했는지 눈으로 보기 쉬움


# 구구단 3단 출력
def gugudan(num): # 매개변수로 함수 정의
    print('-------------------')
    for i in range(1,10):
        print(num,'*',i,'=',num*i)
gugudan(2) # 매개변수가 2인 함수 gugudan 실행
gugudan(5) # 매개변수가 5인 함수 gugudan 실행       


# 1부터 지정한 숫자까지 누적된 값을 출력하는 함수
def hap(num):
    print('합 함수내부코드 :'+str(num))
    sum=0
    for i in range(1,num+1):
        sum = sum + i
    print('1부터',num,'까지의 합은',sum)
    return sum # 지금 계산한 값을 날 호출(실행)한 코드에 전달하고 끝 ->그 밑으로는 실행하지 않음
    print('하하하하하하ㅏ하') # 노란색 밑줄 :데드코드
print(hap(3)) # 함수명은 호출의 의미만 있고 그 값을 불러오지 못함

x = hap(100) # return을 해주지 않으면 None이 됨
y = hap(50)
print(x+y)


# odd(숫자) 1부터 해당 숫자까지 홀수의 누적합
def odd(num): # 매개변수를 사용하여 함수 def 정의
    sum = 0
    for i in range(1,num+1):
        if i%2 != 0:
            sum += i
    print('1부터',num,'까지 홀수의 합은',sum)
    return sum
a = odd(100)
b = odd(30)
print(a+b)


def odd1(num,no): # 매개변수를 여러개 사용할 수 있음, 순서는 콤마로 구분
    sum = 0
    for i in range(1,num+1):
        if i%no == 0:
            sum += i
    print('1부터',num,'까지 홀수의 합은',sum)
    return sum
a = odd1(8,2) # 8까지 2의 배수의 합
b = odd1(9,3) # 9까지 3의 배수의 합
print(a+b)
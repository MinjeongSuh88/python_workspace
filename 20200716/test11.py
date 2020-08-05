print(1+1) # 1+1의 결과값을 출력
a=10
print(a)
a=float(a) # 변수의 자료형을 실수형으로 바꿔서 담음
print(a)
print(complex(1.3, 1.4j)) # 복소수값을 출력
# x=input("아무 값이나 하나 입력하세요")
# print("x의 값은 : "+x)


print(3>5) # 3이 5보다 큰지 논리값 출력
a=100
b=200
print(a<b) # a가 b보다 작은지 논리값 출력
c=None # 변수 c에 None을 담음, 
print(c)
print(100>2 and 300>100) # 100이 2보다 크고 300이 100보다 큰지 논리값 출력
print(100>2 and 300>100 or 100>200) # 100이 2보다 크고 300이 100보다 크거나 100이 200보다 큰지 논리값 출력
x=True
y=False
print(x and y) # 참이 담긴 변수 x 그리고 거짓이 담긴 변수 y의 논리값 출력
print("-------------------------------")
print(True and True) 
print(False or True) # 거짓이거나 참인 논리값 출력
print(not True) # 참이 아닌 논리값 출력 
a=300
b=200
print(a==b) # 변수 a는 변수 b의 같은지 비교한 논리값 출력
print(a!=b) # 변수 a는 변수 b의 같지 않은지 비교한 논리값 출력

# 국어, 영어, 수학 점수를 입력 받아 60점 이하가 있다면 False(실패), True(합격)
kor,eng,mat=input("국어, 영어, 수학의 값을 한 칸씩 띄어 입력하시오").split() # 변수 3개에 사용자로부터 입력받은 값을 스페이스로 구분한 값 대입
print("국어 :",int(kor)>60,", 영어 :",int(eng)>60,", 수학 :",int(mat)>60) # 변수 kor에 넣어 정수로 변환한 값이 60보다 큰지, ... 논리값 출력
print("Total :",int(kor)>60 and int(eng)>60 and int(mat)>60) # 변수 3개에 넣어 정수로 변환한 값이 모두 60보다 큰지 논리값 출력
print("평균 :",(int(kor)+int(eng)+int(mat))/3>60) # 변수 3개에 넣어 정수로 변환한 값의 평균 출력

# 숫자를 입력 받아 2로 나눈 나머지를 출력
# a=int(input("입력하시오"))%2 # a%=2 는 a에 담긴 값을 2로 나눈 나머지를 a에 다시 담음
# print(a)

x,y=input("두 개의 숫자를 입력하세요").split() # split() :입력받은 문자열을 공백을 기준으로 분리시킴
print("x :",x,", y :",y)

# kor,eng,mat=input("국어, 영어, 수학의 점수를 순서대로 쓰시오").split() # 3개의 변수에 사용자로부터 입력한 값을 받는데 구분은 스페이스으로 함
# print("국어 :",kor,", 영어 :",eng,", 수학 :",mat)
# print("총점 :",int(kor)+int(eng)+int(mat),", 평균 :",(int(kor)+int(eng)+int(mat))/3) # 프린트 함수 안에 수식을 직접 넣어 계산할 수 있음
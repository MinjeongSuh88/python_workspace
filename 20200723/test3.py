#map :list나 dictionary와 같은 iterable한 데이터를 인자로 받아 list안의 개별 items을 함수의 인자로 전달하여 결과를 list형태로 주는 내장함수
def func1(x):
    return x*2
m=[10,20,30,40]

# print(map(함수명,iterable 데이터))
''' 이 긴 코딩을 아래와 같이 한 줄로 요약 가능  => for문 사용하는 것을 map으로 요약하고 반복해서 실행할 함수만 정의해서 map(함수명,iterable 데이터)
n=[]
for i in range(len(m)):
    n.append(func1(m[i]))
print(n)    
'''
print(map(func1,m)) # map이라는 함수가 지정됨
print(list(map(func1,m))) # 리스트로 형변환


t={1:100,2:200,3:300}    
'''
for i in t:
    print(func1(i))
for i in t:
    print(func1(t[i]))
'''
print(list(map(func1,t))) # t 딕셔너리의 키값에 func1을 적용
print(list(map(func1,[t[i] for i in t]))) # t 딕셔너리의 밸류값에 func1을 적용


# 3의 배수만 출력
a=[1,2,3,4,5,6,7,8,9,10]
print([i for i in a if i%3==0])

# 3의 배수만 문자형으로 출력
def makeString(x):
    return str(x)
print(list(map(makeString,[i for i in a if i%3==0])))

# 3의 배수만 문자형으로, 나머지는 숫자형으로 출력
def makeString(x):
    if x%3 == 0:
        return str(x)
    else:    
        return x
print(list(map(makeString,a)))
print(list(map(lambda x: str(x) if x%3==0 else x,a)))

# 소수?
def primeNumber(x):
    for i in range(2,x):
        if x % i != 0: # 소수면 실수로 리턴
            return float(x)
        else: # 아니면 자기 자신
            return x
print(primeNumber(7))
# 람다식으로 출력
# print((lambda x: float(x) if x%i !=0 else x),[i for i in range(2,x)])  # 하지마!!리스트 내포 표현식과 필터를 같이 사용?


# filter :조건에 일치하는 값만 추출할 때 사용하는 함수
n=[-3,-2,-1,0,1,2,3]        
def test2(x):
    if x>0 :
        return x
    else:
        return None
print(list(filter(test2,n)))
print(list(filter(lambda x: x>0,n))) # 함수 test2의 기능과 같은 람다 함수 만듦

# 60 이상
score=[80,70,53,90,70,80,49,99]
print(list(filter(lambda x: x>=60, score)))
# 70점 이상 90점 사이 
print(list(filter(lambda x: x>=70 and x<90,score)))


#현재 작업 디렉토리에서 파일들의 목록 가져옴
file_names=['movie1.jpg','movie2.jpg','rabbit.png','bg.png','test.txt','test2.py']
# png파일의 확장자만 검사해서 파일의 이름
def finds(x):
    if x.find('png') != -1:
        return x
    else:
        return None   
print(finds('movie1.png'))
print(list(filter(finds,file_names))) # finds함수로 file_names리스트에서 조건을 만족하는 값들을 걸러와서 리스트로 만들어 출력
print(list(filter(lambda x: x.find('png') != -1,file_names)))# 람다식으로 축약
# print([i for i in file_names if i.find('jpg') != -1])
# lambda x: x.
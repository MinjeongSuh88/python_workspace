import random # 내장되어 있는 것 외에 다른 사람들이 만들어 놓은 것을 불러서 쓸 수 있는 것
for i in range(10):
    print(random.random()) # 0과 1사이의 실수값을 랜덤하게 뽑음
for j in range(10):
    print(random.randint(1,6)) # 1과 6사이의 정수값 


print("----------------------------")
# 로또 번호 6개 출력
m=list(range(1,46))
for i in range(1000):
    a=random.randint(0,44) # 0부터 44 사이의 랜덤 정수값
    b=random.randint(0,44)
# print(m[a])
# print('m[',a,'] :',m[a],', m[',b,'] :',m[b])
# print(m[random.randint(0,44)])
    m[a],m[b]=m[b],m[a] # 리스트 m의 요소들을 1000번 랜덤넘버 의해 섞음
# print('m[',a,'] :',m[a],', m[',b,'] :',m[b])
for j in range(6): 
    print(m[j],end="\t") # 리스트 m의 요소 앞의 6개를 뽑아서 출력
print()


# 로또 번호가 순서대로 출력되게 하기
n=list(range(6)) # 6칸짜리 리스트 만듦
print(n)
for j in range(6): 
    n[j]=m[j] # 리스트 m의 요소 앞에서 6개를 리스트 n에 새로 담기
n.sort()
print("------로또 번호-------")
for i in range(6):
    print(n[i],end='\t')
print()


# 사용자 입력값 횟수만큼 로또 번호 출력
cnt=int(input("몇 번?"))
for k in range(cnt):
    m=list(range(1,46)) # 1부터 45까지의 요소가 담김 리스트 m 만듦
    for i in range(1000): # 변수 i를 1000번 돌리는 반복문 시작
        a=random.randint(0,44) # 변수 a에는 0부터 44까지의 랜덤 정수값이 하나 담김
        b=random.randint(0,44) # 변수 b에는 0부터 44까지의 랜덤 정수값이 하나 담김
        m[a],m[b]=m[b],m[a] # 리스트 m의 요소들을 1000번 섞음
    n=list(range(6)) # 6칸짜리 리스트 만듦
    for j in range(6): # 앞에서 6개 새로운 리스트 담기
        n[j]=m[j]
    n.sort()
    print("------로또 번호-------")
    for i in range(6):
        print(n[i],end='\t')    
    print()    






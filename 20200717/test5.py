# 반복문
a=1
while a != 5: # 조건 !=: 같지 않으면
    print(a) # 처리할 문장
    a += 1 # 조건을 변경할 문장

# k=1
# while True:
#     k += 1
#     print("무한반복",k)

for i in range(5): # i는 0부터 4까지
    for j in range(3): # j는 0부터 2까지
        print("i ",i,"j :",j)
print("------------")        

for i in range(1,10):
    print(i)

for i in range(1,10):
    print("3","*",i,"=",3*i)

for dan in range(2,10): # 이하의 반복문을 2부터 9까지 반복함
    for i in range(1,10):
        print(dan,"*",i,"=",dan*i)
    print("-----------------") # 구분선을 넣어 j의 반복을 확인하기 쉽게

j=0
for i in range(1,5):
    print(j*10+i)
    j=j*10+i

j='*'
for i in range(1,6):
    print(j*i)
print
print("----------")
for j in range(1,5):
    for i in range(5):
        print(j,end="")
    print()
print("----------")
for j in range(1,5): # 선생님 버전
    for i in range(1,j+1):
        print(i,end="")
    print()


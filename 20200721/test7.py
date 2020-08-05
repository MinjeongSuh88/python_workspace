# 리스트 요소 10개를 서로 한 개씩 비교하여 최대값을 뽑아내기
import random

num=[]
for i in range(10):
    num.append(random.randint(1,999)) 

# 최대값을 구해서 출력
temp=0  
for j in range(10): # for j in num: print(j)
    if temp < num[j]: # 임시변수 0보다 리스트 n의 0번째가 크면
        temp = num[j]
print(num, temp)
print(max(num))        

# 최소값을 구해서 출력
temp1=1000
for k in num:
    if k < temp1:
        temp1 = k
print(num, temp1)
print(min(num))        
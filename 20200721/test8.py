m = [3,0,1,8,7,2,5,4,6,9]
print(m)
print(len(m))

# 버블 정렬
# if m[0] > m[1]: # 리스트 m의 0번째 요소가 1번째 요소보다 크면
#     m[0],m[1]=m[1],m[0] # 서로의 값을 바꿈
# print(m)
# if m[1] > m[2]: # 리스트 m의 1번째 요소가 2번째 요소보다 크면
#     m[1],m[2]=m[2],m[1] 
# print(m)
# if m[2] > m[3]: # 리스트 m의 2번째 요소가 3번째 요소보다 크면
#     m[2],m[3]=m[3],m[2]
# print(m)

# 위를 아홉번 반복한 것을 아래와 같이 정리
# for i in range(9):
#     if m[i] > m[i+1]: # 0번째가 1번째보다 클 때부터, 8번째가 9번쨰보다 클 때까지 비교
#         m[i],m[i+1]=m[i+1],m[i]
# print(m)

# # 이걸 9부터 1까지 반복    
# for i in range(8): # 0번째가 1번째보다 클 때부터, 7번째가 8번쨰보다 클 때까지 비교
#     if m[i] > m[i+1]: 
#         m[i],m[i+1]=m[i+1],m[i]
# print(m)
# for i in range(7):
#     if m[i] > m[i+1]:
#         m[i],m[i+1]=m[i+1],m[i]
# print(m)
# for i in range(6):
#     if m[i] > m[i+1]:
#         m[i],m[i+1]=m[i+1],m[i]
# print(m)
# ... range(1) 까지 반복

# 위를 아홉번 반복한 것을 아래와 같이 정리
for j in range(9,0,-1):
    for i in range(j):
        if m[i] > m[i+1]:
            m[i],m[i+1]=m[i+1],m[i]
        print(m)
    print('--------------------')

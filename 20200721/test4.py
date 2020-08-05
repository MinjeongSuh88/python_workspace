# 주사위
for i in range(1,7):
    for j in range(1,7): # 주사위를 2개 돌려사
        if i + j == 4: # 합이 4면
            print('('+str(i)+','+str(j)+')') # 프린트


# 윤년 확인
y = int(input('연도입력:'))
if y % 4 == 0: # 4년 단위 중에
    if y % 100 != 0 or y % 400 == 0: # 100년 단위가 아니거나 400년 단위인 것 중에
        print(str(y)+'년은 윤년입니다.')
else:         
    print(str(y)+'년은 윤년이 아닙니다.')

# 한 줄로 묶으면 if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:


#1부터 100까지 중 3의 배수를 총 다섯개만 출력하고 끝
total = 0
for i in range(1,101):
    if i % 3 == 0:
        total += 1
        print(i)
        if total == 5: # 실행 회수가 6번이 될 때 멈춤
            break


total = 0
for i in range(1,101):
    if i % 3 == 0 and total < 5: # 이렇게 하면 실행을 100번 반복
        total += 1
        print(i)
        
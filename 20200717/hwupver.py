time = int(input("시간입력 : "))
li = [[60, '초'], [60, '분'], [24,'시간']]
word = "입니다."
for i in li:
    print(i[0], i[1])
    word = str(time%i[0]) + i[1] + " " + word
    time = time//i[0]
word = str(time) + "일 " + word;
print(word)



li = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
money = int(input("돈을 넣어 주세요."))

for i in li:
    print(str(i) + "권\t:" + str(money//i) + "매")
    money = money%i

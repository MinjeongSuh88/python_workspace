# 태어난 년도를 입력하면 어떤띠인지 출력 
# 자축인묘진사오미신유술해=쥐소호토용뱀말양원닭개돼
# 4 5 6 7 8 9 10 11 0 1 2 3

birth=int(input('태어난 년도를 4글자로 입력하시오'))
print(birth&12)
if birth % 12 == 4:
    print("당신은 쥐띠")
elif birth % 12 == 5:
    print("당신은 소띠")
elif birth % 12 == 6:
    print("당신은 호랑이띠")
elif birth % 12 == 7:
    print("당신은 토끼띠")
elif birth % 12 == 8:
    print("당신은 용띠")
elif birth % 12 == 9:
    print("당신은 뱀띠")
elif birth % 12 == 10:
    print("당신은 말띠")
elif birth % 12 == 11:
    print("당신은 양띠")
elif birth % 12 == 0:
    print("당신은 원숭이띠")
elif birth % 12 == 1:
    print("당신은 닭띠")
elif birth % 12 == 2:
    print("당신은 개띠")
elif birth % 12 == 3:
    print("당신은 돼지띠")


zodiac=['원숭이띠','닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠','용띠','뱀띠','말띠','양띠']
year=int(input('태어난 년도를 4글자로 입력하시오'))
year %= 12 # year를 12로 나눈 나머지를 year에 다시 담는다
print('당신의 띠는', zodiac[year],'입니다.')
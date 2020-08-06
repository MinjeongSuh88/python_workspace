# 로또 번호 생성기
def getLotto(num):
    for i in range(num):
        lotto=[]
        import random # 랜덤하게 1부터 45사이의 정수 생성
        i = 0
        while i < 6: # 6자리가 모두 완성되면
            r = random.randint(1,45)
            if r in lotto: # 중복된 값이 있으면 다시 뽑음
                continue
            else:
                lotto.append(r) # lotto 리스트에 담음
                i += 1
        lotto.sort() # 정렬 
        return lotto
getLotto(5)



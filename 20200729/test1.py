class Test:
    def __init__(self,balance):
        print('초기화 함수')
        self.balance = balance
    def print(self):
        print('잔액 :',self.balance)

t = Test(500)    
t.aaa = 200 # 인스턴스 t의 주소로 가서 aaa라는 변수가 없으면 만들어서 값을 대입해줌
t.print()
print(t.aaa)
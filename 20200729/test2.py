class ATM:
    def __init__(self):
        print('초기화 함수 호출됨')
        self.__balance = 0 # __변수 :내부에서만 사용되는 변수
        self.name = '홍길동'
    def get__balance(self): # getXXX # 가져오다 -> getter메서드
        # 실제의 경우 감사기록 남음
        print('잔액 :',self.__balance)
    def set__balance(self,balance): # setXXX # 지정하다 -> setter메서드
        #감사기록
        self.__balance == balance
    def deposit(self,money):
        self.__balance += money
        print(money,'원을 입금합니다.')
        print('현재 잔액 :',self.__balance)
    def withDraw(self,money):
        if self.__balance >= money:
            self.__balance -= money
            print(money,'원을 출금합니다.')
        else:
            print('돈이 부족하다.. ^.^')
        print('현재 잔액 :',self.__balance)
auto = ATM()
print(auto)        
auto.deposit(100)
auto.__balance = 99999999999999999999999 # 없는 변수라 생각하여 새로운 변수를 생성
# auto._balance = 99999999999999999999999 # 내부에서 쓰는 변수로 지정해두었기 때문에 외부에서 수정하지 말자는 개발자들끼리의 암묵적 약속(수정은 되긴 함-)
                                          # 은행 같은 경우 변수에 값을 바로 대입하면 로그나 db에 기록이 남지 않기 떄문
print(auto.__balance) # 변수가 없다고 나옴
auto.withDraw(60000000)

auto.get__balance()

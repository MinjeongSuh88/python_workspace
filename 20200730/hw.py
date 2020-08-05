print('---------------문제 1------------------')
# 클래스 :객체의 속성들을 모델링 해놓은 설계도와 같은 것
# 객체 : 프로그램 상의 모든 사물
# 인스턴스 : 클래스로 생성해낸 대상


print('---------------문제 2~9------------------')
class Cat: # 문제 2
    def __init__(self,name,age):
        print('야옹야옹') # 문제3
        self.name = name # 문제5
        self.age = age

    def play(self,what):
        print(what+'을 가지고 놀고 있다냐옹') # 문제4

    def info(self):
        print('이름 :',self.name,', 나이 :',self.age)

    def eat(self,what):
        print(self.name+'가',what+'을 먹고 있어요')

    def __del__(self): # 문제9
        print('고양이 죽는다 야옹')        

# nabi = Cat() # 문제3
# nabi.play('공') #문제 4
nabi2 = Cat('나비',2) #문제5
print(nabi2) # 문제6
nabi2.info() # 문제7
nabi2.eat('생선') # 문제8
del nabi2 


print('---------------문제 10~17------------------')
class Customer():
    def __init__(self,name,age,resiNum): # 문제 10
        self.name = name
        self.age = age
        self.resiNum = resiNum
        self.balance = 0
        self.count = 0
    
    def show(self): # 문제11
        print(self.name+'님 현재 잔액은',str(self.balance)+'원 입니다.')

    def deposit(self,m):
        self.count += 1 # 문제16
        if self.count % 5 != 0:
            self.balance += m
        else:
            self.balance = int((self.balance + m) * 1.05)
        print(self.name+'님 계좌에',str(m)+'원 입금합니다.')
        print(self.name+'님 현재 잔액은',str(self.balance)+'원입니다.')
        
    def withDraw(self,m):
        if m < self.balance: # 문제14
            self.balance -= m  
            print(self.name+'님 계좌에',str(m)+'원 출금합니다.')
        else: # 문제13
            print('잔액이 부족합니다.')    
        print(self.name+'님 현재 잔액은',str(self.balance)+'원입니다.')

    def get_balance(self): # 문제15
        return self.balance

    def set_balance(self,m):
        self.balance = m

    def __del__(self): # 문제17
        print('그 동안 이용해주셔서 감사합니다')
        print('계좌 잔액 :',self.balance)

c = Customer('홍길동',20,'990101-1234567') 
c.show() 
# c.deposit(5000) # 문제12
c.withDraw(9000) 
c.withDraw(2000) 
print(c.get_balance())
c.set_balance(30000)
c.deposit(1000)
c.deposit(3000)
c.deposit(2000)
c.deposit(2000)
c.deposit(3000)
del c


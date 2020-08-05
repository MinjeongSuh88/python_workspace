# import os 
import time
import log

class ATM:
    def __init__(self):
        print('초기화 함수 호출됨')
        self.balance = 0
        self.name = '홍길동'
    def deposit(self,money):
        self.balance += money
        print(money,'원을 입금합니다.')
        print('현재 잔액 :',self.balance)
        log.saveLog('./20200728/bank.log',money,self.balance,False) # 자주 쓰이는 기능(입출금 내역 기록)을 log라는 모듈로 만들어놓고 외부에서 불러와서 사용
        # with open('./20200728/bank.log','a',encoding='utf-8') as file: # 현재 디렉토리에 bank.log 파일을 생성
        #     log = ['입금 내역 - ','현재시간 :',time.ctime(),', 입금액 :',str(money),', 현재잔액 :',str(self.balance),'\n']
        #     file.writelines(log) 
    def withDraw(self,money):
        # db에 연결해서 현재 진짜 잔액이 있는지
        # 권한은 있는지
        # 감사기록을 남김
        if self.balance >= money:
            self.balance -= money
            print(money,'원을 출입금합니다.')
            log.saveLog('./20200728/bank.log',money,self.balance,True)
            # with open('./20200728/bank.log','a',encoding='utf-8') as file: # 현재 디렉토리에 bank.log 파일을 생성
            #     file.write('출금 내역 - '+'현재시간 :'+time.ctime()+', 출금액 :'+str(money)+', 현재잔액 :'+str(self.balance)+'\n') # 현재 시간, 출금액, 현재 잔액 저장
        else:
            print('돈이 부족하다.. ^.^')
        print('현재 잔액 :',self.balance)
auto = ATM()
print(auto)        
auto.deposit(100000000)
auto.withDraw(60000000)


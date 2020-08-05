# 상속 :부모 클래스의 속성, 함수를 상속 받음

class Person:
    '''
    독 스트링
    '''
    def __init__(self): # self :instance의 주소가 매개변수로 들어감
        print(id(self)) # id :주소
        print('초기화 함수')        
        self.name = '홍길동' # 속성인 변수들은 초기화 함수에 선언함
        self.age = 20
        self.job = '도적'

    def eating(self,what): # instance의 주소와 매개 변수가 인자로 전달
        print(self.name,'이',what,'을/를 맛있게 먹어요')

    def sleeping(self):
        print('잠자는 중')  


class SuperMan(Person): # Person이라는 부모 클래스를 상속 받은 SuperMan
    def __init__(self,name,age,job,hobby):
        print('SuperMan 초기화 함수')
        self.name = name
        self.age = age
        self.job = job
        self.hobby = hobby
    
    def fly(self):
        print('빰빠밤빠바바밤')
        print('어린시절 모두 해봤잖아요.. 비행.. .비행청소년')

    def laser(self):
        print('찡~~~~~~~~~~~~~~~~~~~~~~')


sm = SuperMan('슈퍼맨',20,'신문기자','연애')
sm.fly()
sm.eating('바나나')
sm.sleeping()

from test9 import Parent

class Child(Parent):
    def __init__(self):
        print('초기화 함수')
        super().__init__() # 부모의 초기화 변수 불러옴
        self.name = '홍길동'
        self.age = 20
        self.score = 100

    def goClub(self):
        print('둠칫')

    def sing(self): # method overriding :부모가 가진 메서드 내용 바꿈
        print('함께 떠나자~~ 야야야야야 바다로')
        
    
if __name__ == '__main__':
    c = Child()
    print(c.name)
    print(c.age)
    c.sing() # 안쓴다와 물려 받지 않는다는 다른 의미
    c.goClub()
    
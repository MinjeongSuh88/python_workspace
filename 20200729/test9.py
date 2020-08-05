# 부모에서 자식으로 내려가는 것 : 구체화
# 자식에서 부모로 올라가는 것 : 추상화

class Parent:
    def __init__(self):
        print('초기화 함수')
        self.name = '홍판서'
        self.age = 60
        self.height = 160
        self.sex = '남'
        self.country = '조선'
    
    def eat(self):
        print('냠냠')

    def sleep(self):
        print('쿨쿨')

    def sing(self):
        print('아리랑')

    def cook(self):
        print('소금소금')


if __name__ == '__main__':
    p = Parent()
    print(p.name)


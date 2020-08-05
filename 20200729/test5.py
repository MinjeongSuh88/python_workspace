from test7 import Animal

class Monkey(Animal):
    def __init__(self,foots):
        print('초기화 함수')
        self.species = '괼디원숭이'
        self.name = '숭이'
    
    def wash(self):
        print('이를 잡아요')


if __name__ == '__main__':
    m = Monkey(2)
    m.wash()
    m.eating()
    m.sleeping()
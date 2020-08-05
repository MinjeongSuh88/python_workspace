from test7 import Animal

class Whale(Animal):
    def __init__(self,foots):
        print('초기화 함수')
        self.nose = 1
        self.fin = 1
    
    def swim(self):
        print('수영을 해요')
    
    def blow(self):
        print('물을 뿜어요')

if __name__ == '__main__':
    w = Whale(0)
    print('고래 지느러미 :',w.fin)
    w.blow()
    w.eating()
    w.sleeping()
    
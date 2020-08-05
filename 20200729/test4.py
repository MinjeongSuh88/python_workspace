from test7 import Animal
# 부모 클래스, base class, super class, parent
# 자식 클래스, derived class, child
class Rabbit(Animal):
    def __init__(self,foots):
        super().__init__(foots) # 부모의 init을 부름, 부모 init에 self 외의 매개변수가 있을 경우 
        print('초기화 함수')
        self.species = '앙골라'
        self.name = '토순이'

    def jump(self):
        print('깡총깡총 뛰어요')

if __name__ == '__main__':
    r = Rabbit(4) # 매개변수 foots에 인수 전달
    r.jump()
    r.eating()
    r.sleeping()
    print(r.eyes) # 인스턴스 변수는 init에 담겨있기 떄문에 부모 객체의 init를 불러줘야 사용 가능
    print(r.foots)

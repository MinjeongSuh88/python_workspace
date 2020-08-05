'''
OOP(Object Oriented Programming) :객체를 중심으로 한 프로그래밍
    - 자원의 재활용
    - 클래스를 사용해 객체 생성
    - 클래스는 새로운 이름 공간을 지원하는 단위
    - isinstance(변수, 클래스명) :변수가 클래스에서 나온 객체인지 판별
'''
class Car:
    def __init__(self,brand,name,color,year): # 메서드의 첫번째 파라미터명은 관례적으로 self 이름 사용
                                              # 호출시 호출한 객체 자신이 전달되기 때문에 self 이름 사용
        self.brand = brand # instance 변수
        self.name = name
        self.color = color
        self.year = year
        self.wheel = 4
        self.handle = 'black'
    def forward(self): # instance 함수(메서드)
        print('전진 부웅')
    def backward(self):
        print('후진 띠리리리리리리리리')
    def light(self):
        print('깜빡')
    def accelerate(self):
        print('가즈아')
    def brake(self):
        print('정지')
    def status(self):
        print('제조사 :',self.brand)
        print('차명 :',self.name)
        print('색 :',self.color)
        print('년식 :',self.year)
        print('바퀴개수 :',self.wheel)
        print('핸들개수 :',self.handle)

e = Car('KIA','sportage','white',2017)
e.status()
e.forward() # 원래는 자기자신을 매개변수로 넣어야하지만 생략한 것
Car.forward(e)

print(isinstance(e,Car)) # e가 클래스 Car의 객체인지 여부 판별

print('--------다른 차----------')
ns = Car('닛산','맥시마','silver',2019)
ns.status()




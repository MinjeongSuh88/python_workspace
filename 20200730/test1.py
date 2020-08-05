class Car:
    def __init__(self,handle=1,wheel=4,eye=2,nose=1,mouse=1):
        self.handle = handle
        self.wheel = wheel
        self.eye = eye
        self.nose = nose
        self.mouse = mouse
        print('초기화 함수')

    def run(self):
        print(self.wheel,'붕붕카 달리는 중')

    def stop(self):
        print('정지')

    def smell(self,what):
        print(what,'를 맡으면 힘이 솟는 꼬마 자동차~')

    def talk(self):
        print('어디로 갈까요?ㅋ')

    def __add__(self,otherCar): # + 연산을 위하 정형화 함수, 매직 함수
        print('충돌 ㅜㅜ')

    def __sub__(self,otherCar):
        print('빼기')

c1 = Car()
c1.talk()
c1.run()
print(c1.handle)        


class InheritedCar(Car):
    def __init__(self,handle,wheel,eye,nose,mouse):
        super().__init__(handle,wheel,eye,nose,mouse)
        print('초기화 함수')

    def lightOn(self):
        print('라이트를 켜요')        

    def run(self):
        print('나 지금 뚜껑 열였다 달려!!!!!!!!!!!!!')

o1 = InheritedCar(handle=2,wheel=1,eye=2,nose=1,mouse=1)
o1.run()
o1.smell('꽃')
o1.lightOn()
print(o1.handle)


print(c1 + o1)
# 파이썬은 연산자 오버로드가 가능
# 오버로딩(다중 정의) :하나의 연산자 +가 용도에 따라 기능이 달라짐

print(c1 - o1)


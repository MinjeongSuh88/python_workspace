print('-------문제 1--------')
# object :프로그램에서의 모든 사물
# class :현실 세계의 것을 전산으로 가져오기 위해서 그것의 특징을 모델링 해놓은 것
# instance :클래스로 찍어낸 것


print('-------문제 2--------')
class Man:
    def __init__(self):
        print('초기화 함수')
        self.name = '홍길동'
        self.eye = 2
        self.gender = '남'
        self.arm = 2
        self.age = 20
        self.job = '도적'
        self.character = '스틸'

    def steal(self):
        print('내꼬내꼬 다 내꼬얌!!!')
    
    def run(self):
        print('헛둘 헛둘')
    
    def runrun(self):
        print('땀나게 달려요')
    
    def magic_move(self):
        print('동해 번쩍 서해 번쩍')

m = Man()

print(m.name) # 홍길동
print(m.eye) # 2 
print(m.gender)# 남
print(m.arm) # 2
print(m.age) # 20
print(m.job) # 도적
print(m.character)# 스틸 

m.steal() # 내꼬내꼬 다 내꼬얌!!! 
m.run() # "헛둘 헛둘"
m.runrun() # 땀나게 달려요
m.magic_move() # 동해 번쩍 서해 번쩍        


print('-------문제 3--------')
# a-zA-Z0-9, 첫글자에는 _외에 영문만 가능, 특수문자 사용 불가
# 의미 있게 명명


print('-------문제 4--------')
class Triangle:
    def __init__(self,width,height):
        print('초기화 함수')
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height / 2

triangle = Triangle(100,200)
print(triangle.getArea())


print('-------문제 5--------')
class Rectangle:
    def __init__(self,width,height):
        print('초기화 함수')
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height

r = Rectangle(200,300)
print(r.getArea())


print('-------문제 6--------')
# ex6.py 작성


print('-------문제 7--------')
from ex6 import Figure

class Triangle(Figure):
    def __init__(self,width,height):
        print('초기화 함수')
        super().__init__(width,height)
    def getArea(self):
        return self.width * self.height / 2

triangle = Triangle(100,200)
print(triangle.getArea())

class Rectangle(Figure):
    def __init__(self,width,height):
        print('초기화 함수')
        super().__init__(width,height)
    def getArea(self):
        return self.width * self.height

r = Rectangle(200,300)
print(r.getArea())


print('-------문제 8--------')
class Figure:
    def __init__(self,width,height):
        print('초기화 함수')
        self.width = width
        self.height = height
    def getArea(self):
        return '모형의 너비'

class Triangle(Figure):
    def __init__(self,width,height):
        print('초기화 함수')
        super().__init__(width,height)
    def getArea(self):
        return self.width * self.height / 2

triangle = Triangle(100,200)
print(triangle.getArea())

class Rectangle(Figure):
    def __init__(self,width,height):
        print('초기화 함수')
        super().__init__(width,height)
    def getArea(self):
        return self.width * self.height

r = Rectangle(200,300)
print(r.getArea())


print('-------문제 9--------')
import util
print(util.pythagoras(100,100,200,200))


print('-------문제 10--------')
class Point:
    def __init__(self,x,y):
        print('초기화 함수')
        self.x = x
        self.y = y
    def set_x(self,a):
        self.x = a
    def set_y(self,y):
        self.y = y
    def get_xy(self):
        print('(',self.x,',',self.y,')')
    def move(self,x,y):
        self.x = x
        self.y = y
        print('(',self.x,',',self.y,')')
        
p = Point(100,100)
p.set_x(200)
p.set_y(300)
p.get_xy()
p.move(500,300)

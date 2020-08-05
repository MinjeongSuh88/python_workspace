import random
import math

class Agar:
    def __init__(self,color,nickname):
        self.radius = 5
        self.color = color
        self.nickname = nickname
        self.x = random.randint(1,100) # x좌표 
        self.y = random.randint(1,100) # y좌표
        self.weight = 10

    def feeding(self, other):
        if other.weight <= self.weight: # 상대방이 나의 질량보다 작으면
            self.weight += other.weight # 상대방을 먹음
        else:
            self.weight += 17 # 상대방의 질량이 나보다 크면 내가 상대방의 먹이를 먹음
            print('먹이주기')
            
    def merge(self):
        self.weight += 1 # 먹이 먹으면 질량이 커짐
        self.radius += 0.2 # 먹이 먹으면 반지름도 커짐
        print('셀 먹기')

    def split(self):
        print('반띵!!!!!!')
    
    def move(self):
        print('앞으로 고고')
      
    @staticmethod # :인스턴스가 없어도 독립적으로 인수를 받아서 값을 리턴
     # @:데코레이터 -> 미리 약속되어 있음                        
    def getArea(radius):
        return math.pi * radius**2
print(Agar.getArea(50))

    
    
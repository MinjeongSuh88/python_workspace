
class Gun: 
    def __init__(self,name):
        print('M16 장착')

    def fire(self):
        print('빵야')

class Knife: 
    def __init__(self):
        print('이것은 칼')      

    def cut(self):
        print('샥 이건 입에서 나는 소리가 아니야')

class Bomb: 
    def __init__(self,power):
        self.power = power

    def plant(self):
        print('파괴력',self.power,'짜리 폭탄을 설치했습니다')

class Grenade: 
    def __init__(self):
        print('이것은 수류탄')
        
    def throw(self):
        print('쉬웅')

class Player:
    def __init__(self,nick_name,team,gun_name):
        self.nname =  nick_name
        self.team = team
        self.hp = 100
        self.gun = Gun(gun_name) # Composition 관계로 지정
        print('총 장착')
        self.knife = Knife() # Composition 관계로 지정
        print('칼 장착')

    def trigger(self): # 방아쇠를 당기다
        self.gun.fire()

    def swing(self): # 칼을 휘두르다
        self.knife.cut()

    def getBomb(self,bomb): # Aggregation 관계로 지정
        self.bomb = bomb # 클래스 Player에 bomb라는 인스턴스 변수 생성
        print('수류탄 장착')

    def useBomb(self):
        self.bomb.plant()

    def getGrenade(self,grenade): # Aggregation 관계로 지정
        self.grenade = grenade #클래스 Player에 grenade라는 인스턴스 변수 생성
        print('폭탄 획득')

    def useGrenade(self):
        self.grenade.throw()

p1 = Player('미옹','red','내총')
b = Bomb(100)
p1.getBomb(b)
p1.useBomb()
g = Gun('세컨총') # p1이 소유하고 있지 않은 그냥 총
p1.trigger()
p1.swing()


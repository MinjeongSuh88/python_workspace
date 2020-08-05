
class Gun:
    def __init__(self,name,bullet): # 생성자
        self.bullet = bullet # 클래스 Gun의 속성인 총알
        self.name = name # 클래스 Gun의 속성인 이름

    def fire(self): # 클래스 Gun의 메서드 fire는
        if self.bullet >= 1: # 클래스 Gun의 속성인 총알이 1이상 남았을 경우
            self.bullet -= 1 # 클래스 Gun의 속성인 총알을 1개씩 마이너스
            print('빵야') # 총 발사함을 출력으로 대체
        else:
            print('틱(총알 없음..)') # 클래스 Gun의 속성인 총알이 0개 임으로 총알 없음 출력

    def reload(self): # 클래스 Gun의 메서드 reload는
        self.bullet = 20 # 클래스 Gun의 속성 bullet의 값을 20으로 대체
        print('찰카닥') # 장전되는 소리를 출력으로 대체

class Sword: # 클래스 Sword
    def __init__(self,name): # 생성자
        self.name = name # 클래스 Gun의 속성인 이름
        print('이것은 칼') 

    def swing(self):
        print(self.name,'을 휘두릅니다')

class Bomb: 
    def __init__(self,position):
        self.name = '폭탄'
        self.position = position

    def plant(self):
        print(self.position+' 에 폭탄을 설치했습니다')

class Grenade: 
    def __init__(self):
        self.name = '수류탄'
        
    def throw(self):
        print('fire in a hall!!!!!!!!!!!!!!!!!!!!!')

class Player:
    def __init__(self,name,gun_name,bullet,sword_name):
        self.name = name
        self.hp = 100
        self.gun = Gun(gun_name,bullet) # Composition 관계로 지정
        print('총 장착')
        self.sword = Sword(sword_name) # Composition 관계로 지정
        print('칼 장착')

    def trigger(self):  # Player has a Gun
        self.gun.fire()

    def swing(self):
        self.sword.cut()

    def receive(self,weapon): # Aggregation 관계로 지정
        self.weapon = weapon # 클래스 Player에 weapon이라는 새로운 인스턴스 변수 생성 -> 무기를 어느 것으로든 지정 가능
        print(self.weapon.name,'을 획득하였습니다.')

    # def getGrenade(self,grenade): # Aggregation 관계로 지정
    #     self.grenade = grenade
    #     print('폭탄 획득')

    def useBomb(self):
        self.weapon.plant()

    def useGrenade(self):
        self.weapon.throw()

p1 = Player('미옹','AK70',20,'장미칼') # 총과 칼은 장착한 채로 인스턴스 생성 됨
g = Grenade()
b = Bomb('A site')
p1.receive(g)
p1.useGrenade()
p1.receive(b)
p1.useBomb()

class Weapon: # 다양성 -> 각 무기를 사용하는데 필요한 공통적인 명령어를 하나의 클래스로 묶음
    def __init__(self):
        pass
    
    def use(self): # 모든 무기를 사용하겠다는 통칭을 각각의 무기 안에서 오버라이드할 예정
        pass

    def reuse(self): # 무기마다 재사용하는 방법이 다르므로 오버라이드할 예정
        pass

class Gun(Weapon):
    def __init__(self,name,bullet):
        self.bullet = bullet
        self.name = name

    def fire(self):
        if self.bullet >= 1:
            print("빵야~~~~~ ")
            self.bullet -= 1 
        else:
            print("틱~(총알이 없다...)")
    
    def use(self): # 부모로부터 상속 받은 것을 오버라이드(재정의)
        self.fire()

    def reload(self):
        print("찰카닥")
        self.bullet=20

class Sword(Weapon):
    def __init__(self,name):
        self.name = name

    def swing(self):
        print(self.name ,"을 휘두릅니다.")
    
    def use(self): # 부모로부터 상속 받은 것을 오버라이드
        self.swing()

class Grenade(Weapon):
    def __init__(self):
        pass
    
    def throw(self):
        print('fire in the hall!!!!!!!!!!!')

    def use(self):
        self.throw()

class Bomb():
    def __init__(self):
        pass

    def plant(self):
        print('폭탄이 설치되었습니다.')

    def uninstall(self):
        print('폭탄이 해제되었습니다.')

    def use(self):
        self.plant()

    def reuse(self):
        self.uninstall()


class Player:
    def __init__(self, name):
        self.hp = 100
        self.name = name
        self.weapon = None

    def receive(self,weapon):
        self.weapon = weapon

    def use(self):
        self.weapon.use()

    def reuse(self):
        self.weapon.reuse()

    # def reuse(self)

p = Player("홍기동")
s = Sword("엑스칼리버")
g = Gun("AK47",20)
b = Bomb()
g = Grenade()

p.receive(s) # 마지막에 받은 무기만 소지함
p.receive(g)
p.receive(b)
p.use() # 무기변수.use() :같은 결과 출력
p.reuse()


# 수류탄
# 데미지 

# 칼

# 폭탄 

# 총



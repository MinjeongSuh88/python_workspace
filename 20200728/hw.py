print('-------문제 1-------')
class GuGuDan: # 클래스 이름은 공백을 _로 표시하지 않고 카멜표기법(첫글자 대문자)를 사용
    def __init__(self):
        print('초기화 함수 출력')
        self.dan = 2
    def print(self):
        for i in range(1,10):
            print(self.dan,'*',i,'=',self.dan*i)

g = GuGuDan() # 클래스 GuGuDan으로 찍어낸 g라는 instance
g.dan = 3 # g의 인스턴스 변수 dan을 3으로 변경
g.print()



print('-------문제 2-------')
class Marine:
    def __init__(self):
        self.hp = 100 # instance의 생명 100
        self.attackPoint = 4 # instance의 공격력 4
        print('객체 초기화')
    def attack(self,other): # 공격할 상대의 hp 매개 변수 사용
        if other.hp >= 4: # 상대의 hp가 마이너스가 되지 않게 조건 부여
            other.hp -= self.attackPoint # attack을 실행할 때마다 상대방의 hp가 나의 attackPoint만큼 떨어짐
        else :
            print('고마해라.. 마이 아이가') 
        print('체력이 %d 상태입니다' %other.hp)
    def useSteamPack(self): # 약간 마약 같은 느낌 샘영은 떨어지는 대신 체력이 솟음
        if self.hp >= 5: # hp가 마이너스가 되면 못 쓰도록 조건 부여
            print('힘이 솟아요 뿅')
            self.hp -= 5
        else :  
            print('체력이 %d 상태입니다.'%self.hp)
    def move(self):
        print('GoGoGo')
m1 = Marine()
m2 = Marine()

class Ghost:
    def __init__(self):
        print('초기화 함수 출력')
        self.hp = 100
    def cep(self,other):
        other.hp = 0
        print('핵!!!!!!!!!!!!!!!!!!!!!!!!다 죽음, 상대 체력 :',other.hp)



print('-------문제 3--------')
class SiegeTank:
    def __init__(self):
        print('초기화 함수 출력')  
        self.hp = 100
        self.attackPoint = 50      
    def siegeMode(self,other):
        print('공격력 50!!!!!, 상대 체력 :',other.hp)
        other.hp -= 50

class Medic:
    def __init__(self):
        self.hp = 500
        self.x = 0
        self.y = 0   
        self.mp = 50     
        self.healPower = 7
        self.defensivePower = 3
    def heal(self,target):
        if isinstance(target,SiegeTank) == False:
            target.hp += self.healPower
            print('너를 고치노라. 대상의 체력이 7 상승하여',target.hp,'상태입니다.')
        else:
            print('너는 내가 고쳐줄 수 없다. 메롱')
    def move(self):
        self.x += 5
        self.y += 5
        print('고고 레스고, 좌표')
    def hold(self):
        print('현재 위치를 사수합니다')
# for i in range(100):
#     m1.useSteamPack()   
me = Medic()
me.heal(m1)    
ghost = Ghost()
siegeTank = SiegeTank()

print('---마린이 고스트 공격----')
m1.attack(ghost)
print('---메딕이 고스트 치료----')
me.heal(ghost)
print('---고스트가 마린 공격----')
ghost.cep(m1)
print('---고스트가 메딕 공격----')
ghost.cep(me)
print('---고스트가 고스트 공격----')
ghost.cep(ghost)
print('---Ghost ==> SiegeTank ---')
ghost.cep(siegeTank)   
print('---마린 ==> SiegeTank 공격---')
m1.attack(siegeTank)
print('---메딕 ==> SiegeTank 치료---') 
me.heal(siegeTank)
print('---SiegeTank  ==> 마린---')
siegeTank.siegeMode(m1)
print('---SiegeTank  ==> 메딕 ---')
siegeTank.siegeMode(me)           



print('-----문제 4-----')
class TV:
    def __init__(self):
        print('객체 초기화 실행')
    def turnOn(self):
        print('TV가 켜짐')
    def turnOff(self):
        print('TV가 꺼짐')
    def changeChannel(self,n):
        print('채널이',n,'번으로 바뀝니다.')
tv = TV()
tv.turnOn()
tv.turnOff()
tv.changeChannel(7)



print('-----문제 5-----')
class HandPhone:
    def __init__(self):
        self.phone_number = '011-1111-2222'
    def call(self,n):
        print(self.phone_number,'에서',n,'번으로 전화 거는 중')
    def connect_internet(self):
        print('인터넷에 연결되었습니다')
hp = HandPhone()
hp.call('010-1234-5678')    
hp.phone_number = '010-1234-5678'
print(hp.phone_number)
hp.connect_internet()
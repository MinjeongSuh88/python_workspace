import test6 as t6

class Ghost:
    def __init__(self):
        print('초기화 함수 출력')
        self.hp = 100
    def cep(self,other):
        other.hp = 0
        print('핵!!!!!!!!!!!!!!!!!!!!!!!!다 죽음, 상대 체력 :',other.hp)

class SiegeTank:
    def __init__(self):
        print('초기화 함수 출력')  
        self.hp = 100
        self.attackPoint = 50      
    def siegeMode(self,other):
        print('공격력 50!!!!!, 상대 체력 :',other.hp)
        other.hp -= 50
marine = t6.Marine()
medic = t6.Medic()
ghost = Ghost()
siegeTank = SiegeTank()

print('---마린이 고스트 공격----')
marine.attack(ghost)
print('---메딕이 고스트 치료----')
medic.heal(ghost)
print('---고스트가 마린 공격----')
ghost.cep(marine)
print('---고스트가 메딕 공격----')
ghost.cep(medic)
print('---고스트가 고스트 공격----')
ghost.cep(ghost)
print('---Ghost ==> SiegeTank ---')
ghost.cep(siegeTank)   
print('---마린 ==> SiegeTank 공격---')
marine.attack(siegeTank)
print('---메딕 ==> SiegeTank 치료---') 
medic.heal(siegeTank)
print('---SiegeTank  ==> 마린---')
siegeTank.siegeMode(marine)
print('---SiegeTank  ==> 메딕 ---')
siegeTank.siegeMode(medic)
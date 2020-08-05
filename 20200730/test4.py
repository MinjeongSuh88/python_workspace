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

g = Gun('AK47',20) # 클래스 Gun으로 찍어낸 인스턴스인 g
for i in range(30): # 30회 반복
    g.fire() # 인스턴스 g의 메서드 fire 실행
g.reload() # 인스턴스 g의 메서드 reload 실행
g.fire() 

class Police(): # a 'is a' b 인 관계일 때에만 상속을 해야 함 -> 경찰과 총을 'has a'의 관계
    def __init__(self,name,position,age): # 생성자
        # super().__init__('K2',20) 
        self.name = name # 클래스 Police의 속성인 이름
        self.position = position # 클래스 Police의 속성인 직급
        self.age = age # 클래스 Police의 속성인 나이
        # self.gun = None # 디폴트 값으로 총이 없는 상태를 지정

    def receive_gun(self,gun): # 총을 소유하게 하는 함수
        self.gun = gun # 클래스 Police에 새로운 속성 gun을 만듦

    def patrol(self): # 순찰 중을 출력으로 대체한 클래스 Police의 메서드
        print('순찰 중')
    
    def arrest(self,who): # 체포하는 것을 출력으로 대체한 클래스 Police의 메서드
        print(who,'를 체포한다')
    
    def notify_miranda_rights(self): # 미란다 원칙 공지하는 것을 출력으로 대체한 클래스 Police의 메서드
        print('당신은 묵비권을 행사...')

    def eat_donut(self): # 도넛 먹는 것을 출력으로 대체한 클래스 Police의 메서드
        print('냠냠 도넛 중')

    def use_weapon(self): # 총을 사용하는 함수
        if self.gun != None: # 총을 가지고 있을 때만 발사
            self.gun.fire() # receive_gun 메서드에 의해 클래스 Police에서도 생성된 gun속성(클래스 Gun으로부터 상속 받음)의 fire메서드 실행
        else:
            print('없네.. 당황..')

    def drop_gun(self,gun):
        del self.gun

g = Gun('m60리볼버',8)
p = Police('포돌이','순경',20)
p.receive_gun(g) 
p.use_weapon()
# p = Police('미옹','경위',20) # 총을 항상 갖고 있어야하는 상태
# p.eat_donut()        
# p.notify_miranda_rights()
# p.fire()
# p.reload()
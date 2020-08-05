class Player:
    cnt = 0 # 클래스 속성
    bag = [] # 예:아이템함

    def __init__(self,name):
        print('초기화 함수')
        self.name = name # instance 변수
        Player.cnt += 1 # 클래스명.속성명

    def put(self,obj):
        Player.bag.append(obj) # 예:아이템함(클래스 속성)에 아이템을 넣음

    @classmethod # class 메서드
    def getBag(cls): 
        print('아이템',cls.bag) # 클래스 속성(bag)에 접근할 수 있음

    def attack(self,other): # instance 함수
        print(other.name+'를 공격합니다.')

    def greeting(self,other):
        print(other.name+'부모님은 잘 계시니?')

p1 = Player('에코')        
print(p1.cnt)
p1.put('권총') # p1이 아이템함에 권총을 넣어둠

print('--------p2 생성---------')
p2 = Player('야스오')
print(p2.bag) # p2가 p1이 아이템함에 넣어둔 권총을 확인 가능
print(Player.bag) # 인스턴스.를 통해 또는 클래스.를 통해 클래스 속성 확인 가능

print('----class메서드를 통해 class속성에 접근---')
p1.getBag()
p2.getBag()

print('-------cnt 확인--------')
print(p1.cnt)
print(p2.cnt) # 클래스 속성은 인스턴스끼리 공유하기 떄문에 p1과 p2의 cnt값이 같음
              # 캐릭터끼리 물건을 공유할 때 사용

p1.greeting(p2)
p1.attack(p2)
    
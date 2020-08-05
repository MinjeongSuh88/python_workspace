class Human:
    def __init__(self): # instance ko의 주소가 매개변수 self에 대입됨
        print('초기화 함수 호출')
        self.name = '고길동'
        self.age = 30
        self.job = '고위공직자'
        self.eye = 2
        self.mouth = 1
        self.ears = 2
    def eating(self):
        print('냠냠 맛있게 먹었어요')
    def walking(self):
        print('두 발로 걸어요 아장아장')
    def sleeping(self):
        print('쿨쿨 자요')
    def thinking(self):
        print('생각한다 고로 존재한다..')
    def status(self): # 변수를 함수 한 번에 출력
        print('이름 :',self.name)
        print('나이 :',self.age)
        print('직업 :',self.job)
        print('눈 :',self.eye)
        print('입 :',self.mouth)
        print('귀 :',self.ears)

print(Human,id(Human),type(Human))        
ko = Human() # 인스턴스 변수 = 클래스명() -> 클래스의 초기화 함수가 호춣
ko.status()

# 펭수 찍어냄
p = Human() 
p.name = '펭수' # 펭수의 변수 3개만 변경함
p.age = 10
p.job = 'EBS 직장인'
p.status()
# 변수 호출
print(ko.name) # .연산자 의미 :주소를 찾아가
print(ko.age)
print(ko.job)
print(ko.eye)
print(ko.mouth)
print(ko.ears)
# 함수 호출
ko.eating()
ko.walking()
ko.sleeping()
ko.thinking()


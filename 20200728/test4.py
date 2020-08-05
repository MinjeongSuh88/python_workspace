# instance를 만들 때마다 달라지는 변수가 있을 때 :
# 초기화 함수도 함수이기 때문에 매개변수를 줄 수 있음

class Human:
    def __init__(self,a,b,c): # instance ko의 주소가 매개변수 self에 대입됨
        print('초기화 함수 호출')
        self.name = a
        self.age = b
        self.job = c
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

p = Human('펭수',20,'직장인')
p.status()

print('-----------둘리 찍어내기-------------')
d = Human('둘리',10000000,'백수')
d.status()

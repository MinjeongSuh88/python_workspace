class Person:
    '''
    인간 클래스
    '''
    def __init__(self): # self :instance의 주소가 매개변수로 들어감
        print(id(self)) # id :주소
        print('초기화 함수')        
        self.name = '홍길동' # 속성인 변수들은 초기화 함수에 선언함
        self.age = 20
        self.job = '도적'
    def eating(self,what): # instance의 주소와 매개 변수가 인자로 전달
        print(self.name,'이',what,'을/를 맛있게 먹어요')

p1 = Person() # 인간을 하나 찍어냄        
print('id(p1) :',id(p1))
print(p1.name) # instance의 속성을 출력하기 위해서는 instance.속성
print(p1.age)
print(p1.job)
p1.eating('사과')

print('------인간을 또 찍어냄------')
p2 = Person()
print(p2.name) # 변수의 값까지 똑같이 복제됨

print('---------------------')
print('id(p1) :',id(p1),'id(p2) :',id(p2))





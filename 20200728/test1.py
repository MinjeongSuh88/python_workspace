# 프로그램 세계에서는 모든 사물을 object라 함
# 현실 세계의 것을 전산으로 가져오기 위해선 object를 잘 설계한 설계도 class가 필요
# 인간을 예로 들면 속성-정적(눈,코,입,귀,이름,나이),함수-method(생각하기(),잠자기(),말하기()) -> 객체 모델링
# 메모리 상에 실제 만들어진 사례, 대상을 instance

# class 클래스명:
#     속성
#     함수(),method
class Human: # 붕어빵틀
    def __init__(self): #  __로 시작하는 메서드를 매직메서드라 함 -> instance가 생성될 때 제일 처음으로 실행됨
        print('초기화 함수')
    def eating(self): # 메소드에는 매개변수로 꼭 self가 들어가야 함
        print('냠냠 맛있게 먹어요')
    def sleeping(self):
        print('쿨쿨--zz')

hong = Human() # instance :붕어빨틀로 찍어낸 것      hong = new Human() ?
print(hong) 
hong.eating() # instance에 있는 eating 함수를 호출해
hong.sleeping()

print('--------새로운 인간 만들기--------') 
adam = Human() # 원래 있는 class로 찍어냄
print(adam)
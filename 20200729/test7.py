class Animal: # 토끼, 원숭이, 고래의 공통점을 묶은 부모 클래스
    def __init__(self,foots): 
        print('초기화 함수')        
        self.eyes = 2
        self.mouth = 1
        self.ears = 2
        self.foots = foots

    def eating(self): 
        print('당근을 맛있게 먹어요')

    def sleeping(self):
        print('쿨쿨')

if __name__ == '__main__':
    a = Animal()
    print('눈은',a.eyes)
    



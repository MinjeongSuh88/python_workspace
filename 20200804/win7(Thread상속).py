from threading import Thread

class MThread(Thread): # 부모의 쓰레드 속성을 상속 받음
    def __init__(self, who):
        super().__init__()
        self.who = who

# run 함수를 override
    def run(self):
        for i in range(1,100):
            print(str(i)+'미터 달리는 중', self.who)

h1 = MThread('천둥이')
h2 = MThread('각설탕')

h1.start()
h2.start()

threading.join()
print('짝짝짝 축하합니다... Main Thread end')

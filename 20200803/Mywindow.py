import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
import random

# def __init__(a = 100, b = 200):
#     return a+b


# print(add(100,300))

class MyWindow(QMainWindow): # QMainWindow를 상속 받음
    def __init__(self): # MyWindow 클래스 스스로의 초기화 함수
        super().__init__() # 부모 클래스 QMainWindow의 초기화 함수를 가져옴, 매개 변수가 따로 없으므로 초기값? 사용
        self.setWindowTitle('취업지원') # 윈도우 창의 제목 설정
        # self.move(200,200)
        # self.resize(300,300)
        self.setGeometry(200,200,300,300) # 윈도우 창의 x, y, 너비, 높이 한 번에 표기 가능

        self.btn = QPushButton('비법자소서보기',self) # 윈도우 창 안에 버튼 만듦
        self.btn.move(100,100) # 위치 이동
        self.btn.setToolTip('<h3>날 눌러봐!!<h/3') # tooltip :마우스 갖다대면 풍선말 뜨는 것, html 형식
        self.btn.clicked.connect(self.newWindow) # 버튼 클릭 시그널/ 처리 함수 슬랏

        self.show()

    def newWindow(self):
        for i in range(10):
            time.sleep(0.2) # 시간차
            # self.nw = QMainWindow(self) # 부모 창 하나만 뜸
            self.nw = MyWindow2(self) # QMainWindow를 상속 받은 커스턴 윈도우 창
            self.nw.move(random.randint(0,1000),random.randint(0,400)) # 바둑판식 배열
            # self.nw.resize(500,500)
            self.nw.show()
        # self.hide() # 나는 감추고 다른 창만 열어둠


class MyWindow2(QMainWindow):
    def __init__(self,parent): # 매개변수 self외에 newWindow 가 날 부름
        super().__init__(parent) # MyWindow2 상속 받아옴
        self.setGeometry(100,100,300,300)
        self.setWindowTitle('메롱~') # 창 제목
        p_img = QPixmap('./img/melong.png')
        self.lb = QLabel('메롱',self)
        self.lb.setPixmap(p_img)
        self.lb.setGeometry(0,0,200,200)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_()) 

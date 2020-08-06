import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.setWindowTitle('점찍기')       # 창 타이틀     
        self.setGeometry(100,100,800,600)   # 위치와 크기
        self.show()                         # 화면에 보이게 설정
     
    def paintEvent(self,e):                 # 아무 것도 안 하고 화면만 움직여도 이벤트 발생으로 인식
        print('페인트 이벤트 발생')
        print(e)                            # e: 이벤트 대상 객체, 이벤트가 뭐 때문에 생겼는지, 위치 등의 정보 받아옴
        
        qp = QPainter()                     # QPainter 인스턴스 생성
        qp.begin(self)                      # 페인트 준비 시작

        qp.setPen(QPen(Qt.blue,8))          # 펜 설정(펜객체(색상, 픽셀크기)
        qp.drawPoint(self.width()/2, self.height()/2) # 점 찍기(펜위치는 현재창 너비와 높이의 절반)

        qp.end()                            # 페인트 끝

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
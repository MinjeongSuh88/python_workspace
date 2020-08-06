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
        self.setGeometry(1000,100,800,600)  # 위치와 크기
        self.show()                         # 화면에 보이게 설정
     
    def paintEvent(self,e):                 # 화면 그리는 객체에게 더 포함해서 그려달라는 요청
        print('페인트 이벤트 발생')
        qp = QPainter()                     # QPainter 인스턴스 생성
        qp.begin(self)                      # 페인트 준비 시작

        qp.setPen(QPen(Qt.red, 10))         # 펜 설정(빨간색, 10)
        qp.drawLine(100,100,200,200)        # drawLine(x1,y1,x2,y2)

        qp.setPen(QPen(Qt.green,10))        # 펜 다시 설정(초록색, 10)
        qp.drawLine(100,200,200,100)

        qp.end()                            # 페인트 끝

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
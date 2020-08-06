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


        qp.setPen(QPen(Qt.red, 10))         # 펜 설정(레드, 10픽셀)
        qp.drawEllipse(QPointF(220.0,220.0),100,200)        # QPointF(중심점),x,y :F는 실수형

        qp.setPen(QPen(Qt.blue, 10))
        qp.drawEllipse(QPointF(550,220),200,100)

        qp.end()                            # 페인트 끝

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
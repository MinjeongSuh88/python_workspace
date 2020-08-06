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


        qp.setBrush(QColor(255,100,255))    # 컬러 채우기
        qp.setPen(QPen(QColor(100,100,100), 5))         # QColor(펜 컬러): rgb설정
        qp.drawRect(30,30,100,150)          # drawRect(x,y,너비,높이)

        qp.setPen(QPen(Qt.red, 10))
        qp.drawLine(250,100,650,100)
        
        qp.setBrush(QColor(100,100,255))    # 컬러 채우기
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawRect(250,170,100,70)
        qp.setBrush(QColor(100,150,255))    # 컬러 채우기
        qp.drawRect(400,170,100,70)
        qp.setBrush(QColor(255,150,100))    # 컬러 채우기
        qp.drawRect(550,170,100,70)

        qp.setPen(QPen(Qt.green, 8))
        qp.drawRect(250,310,400,70)

        qp.end()                            # 페인트 끝

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
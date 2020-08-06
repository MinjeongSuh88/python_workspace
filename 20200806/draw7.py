import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random as r
import time
import threading

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('작품')       # 창 타이틀     
        self.setGeometry(1000,100,800,600)  # 위치와 크기
        self.show()    

    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
       
        qp.setPen(QColor(0,0,0))
        qp.setFont(QFont('나눔고딕',50))    # 시스템에 있는 글꼴 사용, 50픽셀
        qp.drawText(100,100,'푸른하늘 은하수') # x/y위치,내용

        self.drawOther(qp)

        qp.end()

    def drawOther(self,qp):         # 그림그리는 객체 qp를 매개변수로 받아와야 함
        pen = QPen(Qt.black, 3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(50,50,100,50)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(200,50,300,150)

  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())       
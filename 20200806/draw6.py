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
        for i in range(500):
            # time.sleep(0.5)            # for문 안에 넣으면 그리는 것도 멈춰서 0.01초 후에 한 번에 그려짐
            qp.setPen(QPen(QColor(r.randint(0,255),r.randint(0,255),r.randint(0,255)),r.randint(1,25)))
            qp.drawLine(r.randint(0,800),r.randint(0,600),r.randint(0,800),r.randint(0,600))
        # self.shape()
        # t = threading.Thread(target = self.shape)
        # t.start()
        qp.end()


    # def shape(self):
  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())       
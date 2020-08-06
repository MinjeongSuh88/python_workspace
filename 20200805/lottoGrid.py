import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
from test1lotto import *

class MyWindow(QWidget): # 위젯 안에서만 레이아웃 적용 가능
    def __init__(self):
        super().__init__()
        self.setWindowTitle('로또 번호 추출기')
        self.setGeometry(100,100,1000,500)

        q_img = QPixmap('./img/lotto/q.jpg')
        self.n1 = QLabel('1',self)
        self.n1.setPixmap(q_img)
        
        self.n2 = QLabel('2',self)
        self.n2.setPixmap(q_img)

        self.n3 = QLabel('3',self)
        self.n3.setPixmap(q_img)
        
        self.n4 = QLabel('4',self)
        self.n4.setPixmap(q_img)
        
        self.n5 = QLabel('5',self)
        self.n5.setPixmap(q_img)
        
        self.n6 = QLabel('6',self)
        self.n6.setPixmap(q_img)

        self.btn = QPushButton('두구두구!!',self)
        self.btn.clicked.connect(self.change)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.n1,0,0)
        grid.addWidget(self.n2,0,1)
        grid.addWidget(self.n3,0,2)
        grid.addWidget(self.n4,0,3)
        grid.addWidget(self.n5,0,4)
        grid.addWidget(self.n6,0,5)
        grid.addWidget(self.btn,1,2,1,2)
        # self.btn.setGeometry(500,400,100,50)

        self.show()

     def change(self):
         




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
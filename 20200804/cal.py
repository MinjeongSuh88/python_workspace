import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('계산기')
        re = QLabel(self.Run(),self)
        btn7 = QPushButton('7',self)
        btn7.clicked.connect(self.Run)
        btn8 = QPushButton('8',self)
        btn9 = QPushButton('9',self)
        btnPlus = QPushButton('+',self)
        btn4 = QPushButton('4',self)
        btn5 = QPushButton('5',self)
        btn6 = QPushButton('6',self)
        btnMinus = QPushButton('-',self)
        btn1 = QPushButton('1',self)
        btn2 = QPushButton('2',self)
        btn3 = QPushButton('3',self)
        btnMulti = QPushButton('*',self)
        btn0 = QPushButton('0',self)
        btn00 = QPushButton('00',self)
        btnEqual = QPushButton('+',self)
        btnDivi = QPushButton('/',self)
        
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(re,0,0,1,4)
        grid.addWidget(btn7,1,0)
        grid.addWidget(btn8,1,1)
        grid.addWidget(btn9,1,2)
        grid.addWidget(btnPlus,1,3)
        grid.addWidget(btn4,2,0)
        grid.addWidget(btn5,2,1)
        grid.addWidget(btn6,2,2)
        grid.addWidget(btnMinus,2,3)
        grid.addWidget(btn1,3,0)
        grid.addWidget(btn2,3,1)
        grid.addWidget(btn3,3,2)
        grid.addWidget(btnMulti,3,3)
        grid.addWidget(btn0,4,0)
        grid.addWidget(btn00,4,1)
        grid.addWidget(btnEqual,4,2)
        grid.addWidget(btnDivi,4,3)

        self.show()
        # print('a')

    def Run():
        return 7

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())        
    print('a')
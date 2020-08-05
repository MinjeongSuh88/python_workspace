import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('미옹이의 계산기 뿌잉')
        self.re = QLineEdit('',self)
        self.btn7 = QPushButton('7',self)
        self.btn8 = QPushButton('8',self)
        self.btn9 = QPushButton('9',self)
        self.btnPlus = QPushButton('+',self)
        self.btn4 = QPushButton('4',self)
        self.btn5 = QPushButton('5',self)
        self.btn6 = QPushButton('6',self)
        self.btnMinus = QPushButton('-',self)
        self.btn1 = QPushButton('1',self)
        self.btn2 = QPushButton('2',self)
        self.btn3 = QPushButton('3',self)
        self.btnMulti = QPushButton('*',self)
        self.btn0 = QPushButton('0',self)
        self.btn00 = QPushButton('00',self)
        self.btnEqual = QPushButton('=',self)
        self.btnDivi = QPushButton('/',self)
        
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.re,0,0,1,4)
        # gridList = [7,8,9,'+',4,5,6,'-',1,2,3,'*',0,00,'+','/']
        # cnt = 0
        # for i in range(1,3):
        #     for j in range(0,4):
        #         grid.addWidget(gridList[cnt],i,j)
        #         cnt += 1
        grid.addWidget(self.btn7,1,0)
        grid.addWidget(self.btn9,1,2)
        grid.addWidget(self.btn8,1,1)
        grid.addWidget(self.btnPlus,1,3)
        grid.addWidget(self.btn4,2,0)
        grid.addWidget(self.btn5,2,1)
        grid.addWidget(self.btn6,2,2)
        grid.addWidget(self.btnMinus,2,3)
        grid.addWidget(self.btn1,3,0)
        grid.addWidget(self.btn2,3,1)
        grid.addWidget(self.btn3,3,2)
        grid.addWidget(self.btnMulti,3,3)
        grid.addWidget(self.btn0,4,0)
        grid.addWidget(self.btn00,4,1)
        grid.addWidget(self.btnEqual,4,2)
        grid.addWidget(self.btnDivi,4,3)

        # self.btn7.clicked.connect(self.f7)
        self.btn7.clicked.connect(lambda: self.func('7'))
        self.btn8.clicked.connect(lambda: self.func('8'))
        self.btn9.clicked.connect(lambda: self.func('9'))
        self.btnPlus.clicked.connect(lambda: self.func('+'))
        self.btn4.clicked.connect(lambda: self.func('4'))
        self.btn5.clicked.connect(lambda: self.func('5'))
        self.btn6.clicked.connect(lambda: self.func('6'))
        self.btnMinus.clicked.connect(lambda: self.func('-'))
        self.btn1.clicked.connect(lambda: self.func('1'))
        self.btn2.clicked.connect(lambda: self.func('2'))
        self.btn3.clicked.connect(lambda: self.func('3'))
        self.btnMulti.clicked.connect(lambda: self.func('*'))
        self.btn0.clicked.connect(lambda: self.func('0'))
        self.btn00.clicked.connect(lambda: self.func('00'))
        self.btnDivi.clicked.connect(lambda: self.func('/'))
        self.btnEqual.clicked.connect(self.cal)

        self.show()
    
    def func(self,txt):
        self.re.setText(self.re.text()+txt)

    # def f7(self):
    #     print('눌림')
    #     self.re.setText(self.re.text()+'7')
    # def f8(self):
    #     print('눌림')
    #     self.re.setText(self.re.text()+'8')
    # def f9(self):
    #     print('눌림')
    #     self.re.setText(self.re.text()+'9')

    def cal(self):
        self.re.setText(str(eval(self.re.text())))

    # def mousePressEvent(self,e):
    #     print(e)
    # def keyPressEvent(self,e):
    #     print('키보드 누를 때')
    # def keyReleaseEvent(self,e):
    #     print('키보드 땔 때')
    # def mouseMoveEvent(self,e):
    #     print('마우스 움직일 때')
    # def mouseDoubleClickEvent(self,e):
    #     print('마우스 더블 클릭했을 때')
    # def resizeEvent(self,e):
    #     print('위젯의 크기를 변경할 때')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())        
import sys
from PyQt5.QtGui import QIcon, QPixmap # 거북이 아이콘을 넣기 위하여
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def goUp(self):
        self.label.move(self.label.x(), self.label.y()-2)
    
    def goLeft(self):
        self.label.move(self.label.x()-2, self.label.y())

    def goRight(self):
        self.label.move(self.label.x()+2, self.label.y())

    def goDown(self):
        self.label.move(self.label.x(), self.label.y()+2)

    def initUI(self):
        self.setWindowTitle('게임?')
        self.resize(700,500)

        p_img = QPixmap('turtle.gif') # QPixmap 객체 만듦
        self.label = QLabel('미옹',self)
        self.label.setPixmap(p_img)
        self.label.move(250,200)
        
        upbtn = QPushButton('↑',self)
        upbtn.resize(30,30)
        upbtn.move(335,370)
        upbtn.clicked.connect(self.goUp)
    
        leftbtn = QPushButton('←',self)
        leftbtn.resize(30,30)
        leftbtn.move(305,400)
        leftbtn.clicked.connect(self.goLeft)

        rightbtn = QPushButton('→',self)
        rightbtn.resize(30,30)
        rightbtn.move(365,400)
        rightbtn.clicked.connect(self.goRight)

        downbtn = QPushButton('↓',self)
        downbtn.resize(30,30)
        downbtn.move(335,430)
        downbtn.clicked.connect(self.goDown)

        self.show()

    def keyPressEvent(self,e):
        print(e.key())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

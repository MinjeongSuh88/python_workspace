# 구구단 3단 출력하는 클릭 버튼 만들기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle('구구단 출력하기')
        self.resize(800,600)

        self.le = QLineEdit(self)
        self.le.resize(100,100)
        self.le.move(350,100)
        font = self.le.font()
        font.setPointSize(20)
        self.le.setFont(font)

        btn = QPushButton('클릭',self)
        btn.resize(100,100)
        btn.move(350,300)
        btn.clicked.connect(self.print) # QLabel 모듈 가져옴
        
        self.show()

    def print(self):
        n = int(self.le.text())
        for i in range(1,10):
            print(n,'*',str(i),'=',str(n*i))             


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
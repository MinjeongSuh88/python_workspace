import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        label1 = QLabel('집에 가~~~~~~~~',self)
        font1 = label1.font()
        font1.setPointSize(30)
        label1.move(50,50)
        label1.setFont(font1)

        btn = QPushButton('go',self)
        btn.move(50,400)
        btn.resize(400,40)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('미옹이 월드')
        self.setWindowIcon(QIcon('./img/simson.png'))
        self.resize(500,500)
        self.show() # 가장 마지막 줄에 있어야 만들어놓은 것들이 창에 뜸

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
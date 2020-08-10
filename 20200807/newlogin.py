from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('e:/login.ui',self)       # cmd로 파이썬 형태를 변환은 안 하고 현재 창에 해당 파일을 바로 읽어 와서 로드함
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())
import sys
from PyQt5.QtGui import QIcon, QPixmap # 거북이 아이콘을 넣기 위하여
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QCoreApplication, Qt # Qt :키보드 움직이기 위해
import time

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('게임?')
        self.resize(700,500)

        p_img = QPixmap('kitty.jpg') # QPixmap 객체 만듦
        self.label = QLabel('미옹',self)
        self.label.setPixmap(p_img)
        self.label.move(250,200)

        self.show()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Up: # e.key() :이벤트의 키값, Qt.Key_Up :키보드 위쪽의 키값    
            self.label.move(self.label.x(), self.label.y()-2)

        if e.key() == Qt.Key_Left: # e.key() :이벤트의 키값, Qt.Key_Left :키보드 왼쪽의 키값    
            self.label.move(self.label.x()-2, self.label.y())

        if e.key() == Qt.Key_Right: # e.key() :이벤트의 키값, Qt.Key_Right :키보드 오른쪽의 키값    
            self.label.move(self.label.x()+2, self.label.y())

        if e.key() == Qt.Key_Down: # e.key() :이벤트의 키값, Qt.Key_Down :키보드 아래쪽의 키값    
            self.label.move(self.label.x(), self.label.y()-2)

        if e.key() == Qt.Key_Space: # QT.Key_Space :키보드 스페이스바의 키값
            for i in range(10):
                time.sleep(0.3)
                self.label.move(self.label.x(), self.label.y()-10)
            for i in range(10):
                time.sleep(0.3)
                self.label.move(self.label.x(), self.label.y()+10)
                print('스페이스 눌림')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

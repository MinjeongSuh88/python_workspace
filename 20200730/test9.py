import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton # 모듈 아래 또 다른 모듈
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() # 현재 인스턴스의 이 함수(ui화면 조성) 실행

    def initUI(self):
        btn = QPushButton('나가기',self)
        btn.move(100,100) # 버턴 위치 조정
        btn.resize(500,500) # 버튼 사이즈 조정
        btn.clicked.connect(QCoreApplication.instance().quit) # 클릭하면 '어디'에 연결, %어디=종료
        self.setWindowTitle('미옹이가 만든 윈도우창') # 창 제목
        self.setWindowIcon(QIcon('./img/instagram.png')) # 창 제목 왼쪽 부분 아이콘
        self.move(10,10) # 창이 켜질 때 위치 조정
        self.resize(1000,600) # 창 크기 조정
        self.show() # 창이 보여지는 기능

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
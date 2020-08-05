# 별도의 윈도우 창 만들기?
# 외부의 라이브러리 가져오기 -> gui? 화면구성

import sys
from PyQt5.QtWidgets import QApplication, QWidget # 모듈 아래 또 다른 모듈
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() # 현재 인스턴스의 이 함수(ui화면 조성) 실행

    def initUI(self):
        self.setWindowTitle('내가 만든 윈도우창') # 창 제목
        self.setWindowIcon(QIcon('./img/instagram.png')) # 창 제목 왼쪽 부분 아이콘
        self.move(10,10) # 창이 켜질 때 위치 조정
        self.resize(1000,600) # 창 크기 조정
        self.show() # 창이 보여지는 기능

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
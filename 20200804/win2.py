import sys
from PyQt5.QtWidgets import *

# 윈도우를 생성하는 클래스 :QMainWindow, QWidget, QDialog
# 메인윈도우를 생성하기 위한 클래스 :QMainWindow, QDialog
# QMainWindow :QHBoxLayout, QVBoxLayout 같은 layout 사용할 수 없음(자체 레이아웃 사용)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.show() # 현재 창 보여주기
    
if __name__ == "__main__":
    # QApplication 클래스(PyQt5.QtWigets 모듈)의 인스턴스를 생성
    app = QApplication(sys.argv) # sys.argv 인수를 전달해서
    ex = MyWidget()
    sys.exit(app.exec_()) # 이벤트 루프 실행하다가 종료




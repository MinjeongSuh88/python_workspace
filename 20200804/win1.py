import sys
from PyQt5.QtWidgets import *

# QApplication 클래스(PyQt5.QtWigets 모듈)의 인스턴스를 생성
app = QApplication(sys.argv) # sys.argv 인수를 전달해서
print(app, sys.argv)

def quit():
    print('quit() 호출됨')
    sys.exit(0) # 0일 땐 현재 시스템을 정상 종료, 그 외의 값 비정상 종료

btn = QPushButton('QUIT') # 버튼 생성
btn.show() # 버튼 보여줌 
btn.clicked.connect(quit) # 버튼 클릭하면(이벤트) quit(이벤트 핸들러) 함수 실행

# app.exec_() # 이벤트 루프 실행 중

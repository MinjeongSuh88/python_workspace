# 오늘도 GUI 프로그램 고고
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton  # 위젯 불러옴 :위젯,버튼 만들기
from PyQt5.QtCore import QCoreApplication # 버튼 클릭하면 창이 꺼지게

class MyApp(QWidget): # 위젯 상속받음
    def __init__(self):
        super().__init__() # 부모 변수를 불러옴
        self.initUI() # 클래스 MyApp로 인스턴스를 생성하면 initUI()함수를 바로 실행 

    def initUI(self): # UI :User Interface
        self.setWindowTitle('와.. 금요일이다.. 불금쓰') # 창의 타이틀 지정
        self.resize(1200,800) # 창의 크기 
        self.move(100,100) # 창의 위치

    # 푸쉬 버튼 객체 생성
        btn = QPushButton('출력',self) # 정확히는 인스턴스를 생성 -> 하지만 객체 생성이라 표현
        btn.setText('Print') # 글자 내용이 변함
        btn.resize(300,100)
        btn.move(450,600)
        btn.clicked.connect(self.print) # 괄호 안이 이벤트 핸들러, clicked :클릭을 하면, connect :저런 함수와 연결
        # 이벤트가 발생(클릭, 드래그 등)하면 이벤트를 처리해주는 역할이 필요함 -> 이벤트 핸들러

    # 종료 버튼
        btn2 = QPushButton('exit',self)
        btn2.resize(300,100)
        btn2.move(800,600)
        btn2.clicked.connect(QCoreApplication.instance().quit) # 버튼을 클릭하면 창이 꺼짐 :QCoreApplication에 있는 현재 인스턴스를 종료
        
        self.show() # 화면에 창을 보여지게 설정

    def print(self): # 이벤트 핸들러인 함수 print를 정의한 것
        print('버튼이 눌림.. 왜 눌러.. ^^;')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


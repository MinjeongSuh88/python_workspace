
# 오늘도 GUI 프로그램 고고
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox  # 위젯 불러옴 :위젯,버튼 만들기
from PyQt5.QtCore import QCoreApplication # 버튼 클릭하면 창이 꺼지게

class MyApp(QWidget): # 위젯 상속받음
    def __init__(self):
        super().__init__() # 부모 변수를 불러옴
        self.initUI() # 클래스 MyApp로 인스턴스를 생성하면 initUI()함수를 바로 실행 

    def print(self): # 이벤트 핸들러인 함수 print를 정의한 것
        id = self.leID.text() # text() :사용자가 타자쳤던 내용을 가져옴
        pw = self.lePW.text() # 사용자가 타자쳤던 내용을 가져옴
        print(id, type(id))
        print(pw, type(pw))
        if id == 'aaa' and pw == 'bbb':
            print('로그인 성공')
        else: 
            print('로그인 실패')
        self.leID.setText('') # ID칸이 지워짐
        self.lePW.setText('') # PW칸이 지워짐

    def close(self):
        response = QMessageBox.question(self,'메세지','정말 나갈려구 흐규',QMessageBox.Yes| QMessageBox.No, QMessageBox.No) # default값은 No으로 지정되어 있음
        # QMessagrBox 클래스 :사용자에게 정보를 제공-질문과 응답을  할 수 있는 대화창
        # print('클로즈 함수 호출되고 있음')
        # print(response) # 65536
        if response == QMessageBox.Yes:
            print('나가지마~~~')
            QCoreApplication.instance().quit()

    def initUI(self): # UI :User Interface
        self.setWindowTitle('와.. 금요일이다.. 불금쓰') # 창의 타이틀 지정
        self.resize(1200,800) # 창의 크기 
        self.move(100,100) # 창의 위치

    # Label 2개
        labelID = QLabel('ID',self) # QLabel을 먼저 임포트해옴, labelID은 전역 변수임
        labelPW = QLabel('PW',self)
        labelID.move(300,150)
        labelPW.move(300,250)
        labelID.resize(120,50)
        labelPW.resize(120,50)

    # 글자 크기   
        fontID = labelID.font() # 폰트 객체 만듦
        fontID.setPointSize(20) # 폰트 객체에 글자 크기 20으로 지정
        labelID.setFont(fontID) # 레이블에 폰트 객체 가져몸
        fontPW = labelPW.font()
        fontPW.setPointSize(20)
        labelPW.setFont(fontPW)

    # id,pw 한줄 쓸 수 있는 칸
        self.leID = QLineEdit(self) # 지역 변수에서 모두 인스턴스 변수로 변경
        self.lePW = QLineEdit(self)
        self.leID.move(500,150)
        self.lePW.move(500,250)
        self.leID.resize(120,50)
        self.lePW.resize(120,50)

    # 푸쉬 버튼 객체 생성
        btn = QPushButton('출력',self) # 정확히는 인스턴스를 생성 -> 하지만 객체 생성이라 표현
        btn.setText('Print') # 글자 내용이 변함
        btn.resize(300,100)
        btn.move(260,600)
        btn.clicked.connect(self.print) # 괄호 안이 이벤트 핸들러, clicked :클릭을 하면, connect :저런 함수와 연결
        # 이벤트가 발생(클릭, 드래그 등)하면 이벤트를 처리해주는 역할이 필요함 -> 이벤트 핸들러

    # 종료 버튼
        btn2 = QPushButton('exit',self)
        btn2.resize(300,100)
        btn2.move(610,600)
        # btn2.clicked.connect(QCoreApplicaton.instance().quit) # 버튼을 클릭하면 창이 꺼짐 :QCoreApplication에 있는 현재 인스턴스를 종료
        btn2.clicked.connect(self.close) # 새로운 함수 명명
        
        self.show() # 화면에 창을 보여지게 설정
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



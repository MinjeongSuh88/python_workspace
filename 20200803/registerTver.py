import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cx_Oracle

class MyApp(QWidget):
    # 레이아웃 :BoxLayout, 수평 상자 수직 상자
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    # QLine Edit
        self.leId = QLineEdit(self) # 아이디 값 받아와서 다른 곳에서 사용할 것이기 때문에 self 전역변수로 지정
        self.lePw = QLineEdit(self)

        self.btnLogin = QPushButton('로그인',self)
        self.btnReg = QPushButton('회원가입',self)

    # 회원가입 버튼 누르면 창 뜨게하기        
    # PyQt에서 이벤트(Signal) 처리할 때 사용되는 함수를 이벤트 핸들러(slot)이라고 한다.
    # Signal
        self.btnLogin.clicked.connect(self.dbCheck)
        self.btnReg.clicked.connect(self.register)

        self.labelId = QLabel('ID',self)
        self.labelPw = QLabel('PW',self)

    # 수평상자 레이아웃 객체, 유동적 위치 조정
        hbox = QHBoxLayout() # Horizontal
        hbox.addStretch(1) # 수평상자 넣음(패딩 개념)
        hbox.addWidget(self.labelId)
        hbox.addWidget(self.leId)
        hbox.addStretch(1) # 수평상자 넣음(패딩 개념)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.labelPw)
        hbox2.addWidget(self.lePw)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.btnLogin)
        hbox3.addWidget(self.btnReg)
        hbox3.addStretch(1)

        vbox = QVBoxLayout() # 열 맞춤?
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    # 창 타이틀 지정
        self.setWindowTitle('로그인')
    
    # 창 사이즈 결정
        self.resize(500,500)
    # 창 위치 결정
        self.move(700,400) # 절대 위치
    # 화면에 보여지게 설정
        self.show()

# slot
    def dbCheck(self):
        print('로그인 버튼 눌림')
    # 1. conneciton 객체 생성
        connection = cx_Oracle.connect('scott','tiger','192.168.0.68:1521/orcl')
        # print(connection)
    # 2.cursor 객체
        cur = connection.cursor()
    # 3. 사용할 sql문 객체
        sql = '''
        select id,pw,name,grade
        from member
        where id = :dbid and pw = :dbpw
        '''
    # 4. 실행
        cur.execute(sql,dbid=self.leId.text(),dbpw=self.lePw.text()) # 사용자로부터 입력받은 id/pw로 로그인하기
        print(cur)
    # 5. 로직처리
        for dbid,dbpw,name,grade in cur:
            print(dbid,dbpw)
            if dbid!=None:
                print('로그인성공')
                # 메세지 박스
                rep = QMessageBox.question(self,'로그인 성공','환영합니다.',QMessageBox.Yes)

    # 6. 자원 반납
        connection.close()

    def register(self):
        print('회원가입 버튼 눌림')
        self.nw = MyRegisterWindow(self) # 매개변수가 있는 MyRegisterWindow 의 초기화 함수를 호출 (현재창)
        self.nw.show()


class MyWidget(QWidget): # 대체관리자? -> 박스 위젯
    def __init__(self):
        super().__init__()


class MyRegisterWindow(QMainWindow):
    def __init__(self, parent): # 매개변수 parent 
        super().__init__(parent)
        self.setCentralWidget(MyWidget()) # MyRegisterWindow를 박스 위젯 MyWidget을 넣음
        # self.initUI()
    # def initUI(self):
        self.setGeometry(50,50,500,600)
        self.setWindowTitle('회원가입')
        self.lb2Id = QLabel('ID',self)
        self.lb2Id.setGeometry(50,50,100,40)
        self.lb2Pw = QLabel('PW',self)
        self.lb2Pw.setGeometry(50,150,100,40)
        self.lbName = QLabel('NAME',self)
        self.lbName.setGeometry(50,250,100,40)

        self.leId = QLineEdit(self)
        self.leId.setGeometry(250,50,100,40)
        self.lePw = QLineEdit(self)
        self.lePw.setGeometry(250,150,100,40)
        self.leName = QLineEdit(self)
        self.leName.setGeometry(250,250,100,40)

        self.btnReg = QPushButton('가입하기',self)
        self.btnReg.setGeometry(200,350,100,40)
        self.btnReg.clicked.connect(self.myregister)

    def myregister(self):
        print('회원가입')
    # 1. conneciton 객체 생성
        connection = cx_Oracle.connect('scott','tiger','192.168.0.68:1521/orcl')
        print(connection)
    # 2.cursor 객체
        cur = connection.cursor()
    # 3. 사용할 sql문 객체
        sql = '''
        insert into member values(:id,:pw,:name,1)
        '''
    # 4. 실행
        cur.execute(sql,id=self.leId.text(),pw=self.lePw.text(),name=self.leName.text()) # 사용자로부터 입력받은 id/pw로 로그인하기     # execute :엔터와 비슷
        connection.commit() # 연결 작
        print(cur)
    # 5. 로직처리
    # 6. 자원 반납
        connection.close()
        self.hide()
# 현재 파일에서 호출시에만 실행가능하게 설정
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit = (app.exec_())
            
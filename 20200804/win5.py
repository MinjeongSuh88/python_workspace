import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
import cx_Oracle
from DbConnect import DbConnect # 파일(모듈)로부터 클래스 불러옴

class MyWidget(QWidget):
    def __init__(self,parent): # 여기서 parent는 MyRegisterWindow를 의미
        super().__init__()
        self.parent = parent # 내 부모는 MyRegister는 인식표
        self.initUI()
     
    def initUI(self):
        self.setGeometry(50,50,500,600)
        self.setWindowTitle("회원가입")
        self.lb2Id = QLabel("ID", self)
        self.lb2Pw = QLabel("PW", self)
        self.lb2Name = QLabel("NAME", self)
        self.le2Id = QLineEdit(self)
        self.le2Pw = QLineEdit(self)
        self.le2Name = QLineEdit(self)
        self.btn = QPushButton("가입하기", self)
        
        self.btn.clicked.connect(self.myregister)
        grid = QGridLayout() # 배치관리자(그리드 레이아웃) 객체 생성
        self.setLayout(grid) # 그리드 레이아웃을 적용

        grid.addWidget(self.lb2Id,0,0) # 객체,행,열
        grid.addWidget(self.le2Id,0,1) # 객체,행,열
        grid.addWidget(self.lb2Pw,1,0) # 객체,행,열
        grid.addWidget(self.le2Pw,1,1) # 객체,행,열
        grid.addWidget(self.lb2Name,2,0) # 객체,행,열
        grid.addWidget(self.le2Name,2,1) # 객체,행,열
        grid.addWidget(self.btn,3,0,1,2) # 객체,행,열,rowSpan,colSpan

    def myregister(self):
        print("회원 가입.. ")
        db = DbConnect('192.168.0.68','orcl','scott','tiger','1521')
        resultLIst = db.execute('select * from emp') # 리턴값이 리스트인 것을 resultList에 담음
        for x in resultList:
            print(x)
        self.parent.close()

    # # 1. connection 객체 생성 
    #     connection = cx_Oracle.connect("scott", "tiger", "192.168.0.68:1521/orcl")
    #     print(connection)
    # # 2. cursor 객체 
    #     cur = connection.cursor()
    # # 3. 사용할 sql문 객체 
    #     sql = """
    #     INSERT INTO member VALUES (:id, :pw, :name, 1)
    #     """
    #  # 4. 실행 
    #     cur.execute(sql,id=self.le2Id.text() , pw=self.le2Pw.text(), 
    #     name=self.le2Name.text())
    #     connection.commit()    
    # # 6. 자원반납 
    #     connection.close()
    #     # self.close() # MyWidget 창만 닫음

class MyRegisterWindow(QMainWindow):
    def __init__(self, parent): # 여기서 parent는 MyApp을 의미
        super().__init__(parent)
        self.setGeometry(50,50,300,400)
        self.setCentralWidget(MyWidget(self)) # 마이위젯을 여기에 넣음
        

class MyApp(QWidget):
    # LayOut  : BoxLayout , 수평 상자 수직 상자 
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI (self):
        #PyQt 에서  이벤트 (Signal)처리할때 
        # 사용되는 함수를 이벤트 핸들러(slot)
        #이라고 한다. 

        self.labelId = QLabel("ID", self)
        self.labelPw = QLabel("PW", self)

        # QLineEdit 
        self.leId = QLineEdit(self)
        self.lePw = QLineEdit(self)

        self.btnLogin = QPushButton("로그인", self)
        self.btnReg  = QPushButton("회원가입", self)    

        #수평상자 레이아웃 객체 
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.labelId)
        hbox.addWidget(self.leId)
        hbox.addStretch(1)

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

        vbox = QVBoxLayout()
#        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
#       vbox.addStretch(1)
        self.setLayout(vbox)
        # signal
        self.btnLogin.clicked.connect(self.dbCheck)
        self.btnReg.clicked.connect(self.register)

    # 창 타이틀 지정 
        self.setWindowTitle("로그인")
    # 창 사이즈 결정
        self.resize(300,300)
    # 창 위치 결정 
        self.move(300,400)
        # 화면에 보여지게 설정 
        self.show()
    def dbCheck(self):
        print("로그인 버튼 눌림")
        # 1. connection 객체 생성 
        connection = cx_Oracle.connect("scott", "tiger", "192.168.0.68:1521/orcl")
        print(connection)
        # 2. cursor 객체 
        cur = connection.cursor()
        
        # 3. 사용할 sql문 객체 
        sql = """
        SELECT id, pw , name , grade 
        FROM member
        WHERE id = :id and pw = :pw
        """
        # 4. 실행 
        cur.execute(sql,id=self.leId.text(), pw=self.lePw.text())
        #print(cur)
        # 5. 로직처리  
        for dbid, dbpw, name , grade in cur:
            print(dbid, dbpw)
            if dbid!=None:
                rep = QMessageBox.question(self,
                "로그인성공", "환영합니다.", QMessageBox.Yes)
                
                #print("로그인성공")
                # 메세지 박스  
        # 6. 자원반납 
        connection.close()


    def register(self):
        print("회원가입 버튼 눌림")
        # MyRegisterWindow 매개변수가 있는 초기화 함수 호출
        self.nw = MyRegisterWindow(self) 
        self.nw.show()
    



# 현재 파일에서 호출시에만 실행가능하게 설정 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



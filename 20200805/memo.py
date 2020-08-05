import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit) # textEdit객체를 중앙에 위치
        self.setGeometry(100,100,600,400)
        self.setWindowTitle('제목 없음 - Windows 메모장')
        self.setWindowIcon(QIcon('./img/memo.jpeg'))
        self.show()

        # 메뉴바 만들기 - 새파일, 열기, 저장, 종료
        openFile = QAction(QIcon('./img/instagram.png'),'열기',self) # 메뉴바-File 아래에 열기 객체 만듦
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('새 파일 열기')
        openFile.triggered.connect(self.showDialog) # 방아쇠

        newFile = QAction(QIcon('./img/melong.png'),'새파일',self) # 메뉴바-File 아래에 새파일 객체 만듦
        newFile.setShortcut('Ctrl+N')
        newFile.setStatusTip('새 파일 만들기')
        newFile.triggered.connect(self.newFile) # 방아쇠
        
        saveFile = QAction(QIcon('.img/somson.png'),'저장',self) # 메뉴바-File 아래에 저장 객체 만듦
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('저장하기')
        saveFile.triggered.connect(self.saveDialog) # 방아쇠

        exitFile = QAction(QIcon('.img/somson/png'),'종료',self) # 메뉴바-File 아래에 종료 객체 만듦
        exitFile.setShortcut('Ctrl+X')
        exitFile.setStatusTip('종료하기')
        exitFile.triggered.connect(QCoreApplication.instance().quit) # 창 종료

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) # 전통적인 메뉴바 안 쓴다
        fileMenu = menubar.addMenu('&File') # 메뉴바 만듦
        fileMenu.addAction(openFile) # 만들어놓은 열기 객체 추가
        fileMenu.addAction(newFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitFile)

        # 메뉴바-서식 만들기
        fontMenu = QAction(QIcon('./img/font.png'),'폰트',self)
        fontMenu.setShortcut('Ctrl+F')
        fontMenu.setStatusTip('글꼴')
        fontMenu.triggered.connect(self.changeFont) 

        formMenu = menubar.addMenu('&서식')
        formMenu.addAction(fontMenu)

    def changeFont(self):
        # print('글꼴 누름')
        font, ok = QFontDialog.getFont() # 만들어 놓은 함수 사용하여 글씨체와 변경 여부 가져옴
        if ok:
            self.textEdit.setFont(font)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'open file','./') # open file :다이얼로그 창 이름
        print('show dialog 함수 호출됨')
        print(fname)
        
        if fname[0]:
            f = open(fname[0],'r',encoding='utf-8')
            with f:
                data = f.read()
                self.textEdit.setText(data)
                name = fname[0].split('/')
                print(name[-1].split('.')[0])
                self.setWindowTitle(name[-1].split('.')[0] + ' Windows 메모장')

    def saveDialog(self):
        # 저장창을 띄우기
        file = QFileDialog.getSaveFileName(self,'저장해봐~~','./') # 저장하는 창 다이얼로그
        print(file)
        # file I/O
        with open(file[0],'w') as f:
            f.write(self.textEdit.toPlainText()) # toPlainText() :textEdit객체에서 문자열만 뽑아냄


    def newFile(self):
        # 기존에 있는 텍스트를 초기화
        print('new dialog 함수 호출됨')
        # textEdit에 내용이 있는지 판단
        # 내용이 존재한다면
        if len(self.textEdit.toPlainText()) != 0:
        # 저장할 것인지를 물어보기, 저장한 후에 지우기
            rep = QMessageBox.question(self,'메모장','변경 내용을 제목 없음에 저장하시겠습니까?',QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
            if rep == QMessageBox.Yes:
                self.saveDialog()
        # 내용이 없으면 그냥 지우기
        self.textEdit.setText('')

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my = MyApp() # 내가 만든 클래스의 객체 생성
    sys.exit(app.exec_())
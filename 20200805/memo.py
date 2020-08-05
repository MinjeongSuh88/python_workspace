import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

        openFile = QAction(QIcon('./img/instagram.png'),'열기',self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('새 파일 열기')

        newFile = QAction(QIcon('./img/melong.png'),'새파일',self)
        newFile.setShortcut('Ctrl+N')
        newFile.setStatusTip('뭐')
        
        saveFile = QAction(QIcon('.img/somson.png'),'저장',self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('')

        exitFile = QAction(QIcon('.img/somson/png'),'종료',self)
        exitFile.setShortcut('Ctrl+X')
        exitFile.setStatusTip('')

        # 메뉴바 만들기 - 새파일, 열기, 저장, 종료
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) # 전통적인 메뉴바 안 쓴다
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(newFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitFile)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my = MyApp() # 내가 만든 클래스의 객체 생성
    sys.exit(app.exec_())
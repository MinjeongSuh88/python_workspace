import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget): # QWidget 상속 받은 MyApp 클래스
    def __init__(self): # 초기화 함수
        super().__init__() # 부모 
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,1000,800)
        # 전체 폼
        frmbox = QHBoxLayout()
        self.setLayout(frmbox) # 현재창에 frmbox 레이아웃 적용

        # 좌측 레이아웃
        leftbox = QVBoxLayout()
        rightbox = QVBoxLayout()

        # 좌측 레이아웃
        gb = QGroupBox('타입')
        leftbox.addWidget(gb) # leftbox에 gb 위젯 추가

        box1 = QVBoxLayout()
        gb.setLayout(box1) # 그룹박스에 수직박스레이아웃 적용

        box1.addWidget(QRadioButton('선',self)) # 그룹      
        box1.addWidget(QRadioButton('곡선',self)) # 그룹      
        box1.addWidget(QRadioButton('사각형',self)) # 그룹      
        box1.addWidget(QRadioButton('타원',self)) # 그룹      

        # 그룹박스2
        gb2 = QGroupBox('Pen setting')
        leftbox.addWidget(gb2)

        grid = QGridLayout() 
        gb2.setLayout(grid) # gb2에 그리드 형식 적용

        label = QLabel('선굵기')
        grid.addWidget(label,0,0) # 0행 0열에 레이블 위젯 추가

        combo = QComboBox()
        grid.addWidget(combo,0,1)
        for i in range(1,21):
            combo.addItem(str(i))

        label2 = QLabel('선색')
        grid.addWidget(label2,1,0)

        # 펜 색상
        self.pencolor = QColor(0,0,0) # self를 붙여서 전역변수 화
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet('background-color:rgb(0,0,0)') # css형식으로 스타일 지정

        grid.addWidget(self.penbtn,1,1)

        # 그룹 박스 3
        # 부 설정
        gb3 = QGroupBox('부 설정')
        leftbox.addWidget(gb3)

        hbox = QHBoxLayout()
        gb3.setLayout(hbox)

        label3 = QLabel('부 색상')
        hbox.addWidget(label3)

        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet('background-color:rgb(255,255,255)')
        hbox.addWidget(self.brushbtn)

        # 우측 레이아웃 박스에 그래픽 뷰 추가
        self.view = CGView(self) # 그래픽 뷰 객체 생성
        rightbox.addWidget(self.view) 

        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)

        self.show()

# QGraphics는 시각적 객체의 복잡한 장면을 쉽게 처리
# 할 수 있는 프레임 워크로 구성하는데 사용할 수 있다.

# QGraphicsView,

class CGView(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.item = []
        self.start = QPointF() # 시작 위치
        self.end = QPointF()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())
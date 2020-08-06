import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget): # QWidget 상속 받은 MyApp 클래스
    def __init__(self): # 초기화 함수
        super().__init__() # 부모 
        self.drawType = 2      # 1. 직선, 2. 사각형
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

        self.rbtnLine = QRadioButton('직선',self)
        self.rbtnRect = QRadioButton('사각형',self)
        self.rbtnCurve = QRadioButton('곡선',self)
        self.rbtnEllipse = QRadioButton('타원',self)
        
        box1.addWidget(self.rbtnLine)       # 수직 박스에 직선 라디오 버튼 위젯 추가 
        box1.addWidget(self.rbtnRect) # 그룹      
        box1.addWidget(self.rbtnCurve) # 그룹      
        box1.addWidget(self.rbtnEllipse) # 그룹      

        self.rbtnLine.clicked.connect(self.radioBtnClicked)
        self.rbtnRect.clicked.connect(self.radioBtnClicked)
        self.rbtnCurve.clicked.connect(self.radioBtnClicked)
        self.rbtnEllipse.clicked.connect(self.radioBtnClicked)

        self.rbtnLine.setChecked(True)      # 기본으로 직선 라디오버튼에 체크되어져 있또도록 설정
        self.drawType = 1                   


    # 그룹박스2
        gb2 = QGroupBox('Pen setting')
        leftbox.addWidget(gb2)

        grid = QGridLayout() 
        gb2.setLayout(grid) # gb2에 그리드 형식 적용

        label = QLabel('선굵기')
        grid.addWidget(label,0,0) # 0행 0열에 레이블 위젯 추가

        self.combo = QComboBox()           # combo는 인스턴스 변수가 됨
        grid.addWidget(self.combo,0,1)
        for i in range(1,21):
            self.combo.addItem(str(i))

        label2 = QLabel('선색')
        grid.addWidget(label2,1,0)

    # 펜 색상
        self.pencolor = QColor(0,0,0) # self를 붙여서 전역변수 화
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet('background-color:rgb(0,0,0)') # css형식으로 스타일 지정
        grid.addWidget(self.penbtn,1,1)

        self.penbtn.clicked.connect(self.selectColorDialog)        # 색상 선택 버튼 누르면 팔레트 뜨도록 하기

    # 그룹 박스 3
    # 붓 설정
        gb3 = QGroupBox('붓 설정')
        leftbox.addWidget(gb3)

        hbox = QHBoxLayout()
        gb3.setLayout(hbox)

        label3 = QLabel('붓 색상')
        hbox.addWidget(label3)

        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet('background-color:rgb(255,255,255)')
        hbox.addWidget(self.brushbtn)

        self.brushbtn.clicked.connect(self.selectColorDialog)       # 붓색상 선택

    # 그룹 박스 4
    # 지우개 - 사각 지우개, 올 클리어
        gb4 = QGroupBox('지우개')
        leftbox.addWidget(gb4)

        hbox4 = QVBoxLayout()
        gb4.setLayout(hbox4)

        self.ers = QPushButton('지우기',self)
        self.ersa = QPushButton('리셋',self)
        hbox4.addWidget(self.ers)
        self.ers.clicked.connect(lambda: self.erase('5'))
        hbox4.addWidget(self.ersa)
        # self.erz.clicked.connect(self.eraseall)
        

    # 그룹 박스 5
    # 파일 저장
        gb5 = QGroupBox('File')
        leftbox.addWidget(gb5)

        hbox5 = QHBoxLayout()
        gb5.setLayout(hbox5)

        saveBtn = QPushButton('버튼',self)
        hbox5.addWidget(saveBtn)
        saveBtn.clicked.connect(self.save_img)

        # 우측 레이아웃 박스에 그래픽 뷰 추가
        self.view = CGView(self) # 그래픽 뷰 객체 생성
        rightbox.addWidget(self.view) 

        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)

        self.show()

    def save_img(self):
        img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))        # 현재 뷰에서 씬을 사각형 모양으로 잡아서 이미지 객체로 만듦 
        # print(img)
        # img.save('e:/data.png')     # 2줄로 파일이 저장됨
    # 파일 선택헤서 이 이미지 저장할 수?
        fname = QFileDialog.getSaveFileName(self,'어따 저장할래?','./')     # ./?
        print(fname)
        if fname[0]:
            img.save(fname[0])

    def erase(self,n):
        self.drawType = int(n)
        print('선택된 타입은 :',self.drawType)


    def selectColorDialog(self):
        # 색상 대화상자 생성
        color = QColorDialog.getColor()     # 컬러 정할 수 있는 내장 함수
        # print(self.sender())        # 선색과 붓색상의 주소가 다름 -> <PyQt5.QtWidgets.QPushButton object at 0x00000254C38EE3A0>
        who = self.sender()
        if who == self.penbtn:
            self.pencolor = color
            self.penbtn.setStyleSheet('background-color:{}'.format(color.name()))
            # print('팬 버튼이었어')
        elif who == self.brushbtn:
            self.brushcolor = color
            self.brushbtn.setStyleSheet('background-color:{}'.format(color.name()))
            # print('붓 색상 버튼이었어')            


    def radioBtnClicked(self):      # 어떤 라디오 버튼이 선택 됬는지 판단
        if self.rbtnLine.isChecked():        # 이 버튼이 선택되었다면 drawType은 1
            self.drawType = 1
        elif self.rbtnRect.isChecked():        # 이 버튼이 선택되었다면 2
            self.drawType = 2
        elif self.rbtnCurve.isChecked():        # 이 버튼이 선택되었다면 3
            self.drawType = 3
        elif self.rbtnEllipse.isChecked():        # 이 버튼이 선택되었다면 4
            self.drawType = 4
        print('선택된 타입은 :',self.drawType)
        

# QGraphics는 시각적 객체의 복잡한 장면을 쉽게 처리
# 할 수 있는 프레임 워크로 구성하는데 사용할 수 있다.
# QGraphicsView, QGraphicsScene, QGraphicsItems

class CGView(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF() # 시작 위치
        self.end = QPointF()

    def moveEvent(self, e):             # 창 크기 변경할 때 호출 됨
        # print('moveEvent 호출됨')
        rect = QRectF(self.rect())      # 현재 자신의 크기
        rect.adjust(0,0,-3,-3)          # 시작점,크기는 3씩 작게
        self.scene.setSceneRect(rect)

    def mousePressEvent(self,e):        # 매개변수 e: event의 약어
        # print('마우스 클릭됨')
        if e.button() == Qt.LeftButton: # 왼쪽 버튼(Qt.leftButton) -> 1, 오른쪽 버튼 -> 2, 휠  -> 4
            self.start = e.pos()        # 시작점 저장
            self.end = e.pos()
            # print(e.pos())              # PyQt5.QtCore.QPoint(469, 322)

    def mouseMoveEvent(self,e):         # 마우스 드래그 할 때
        print('마우스가 드래그 됨', self.parent().drawType )
        self.end = e.pos()
        # pen = QPen()    # 펜 객체 만듦, 기본은 검정색
        pen = QPen(self.parent().pencolor,self.parent().combo.currentIndex()+1)       # 부모(MyApp)의 인스턴스 변수 가져옴
        # print(self.parent().combo.currentIndex)

        if len(self.items) > 0 :        # Scene에 그려진 이전 선을 제거
            # print(self.items)       
            self.scene.removeItem(self.items[-1]) # Scene 상에서 그림을 지우고
            del(self.items[-1])         # 리스트 상에서 
        
    # 선 그리기
        if self.parent().drawType == 1:
            line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())   # 현재 선을 추가
            self.items.append(self.scene.addLine(line, pen))        # 빈 리스트에 라인 객체 모두 담음
    # 사각형 그리기
        elif self.parent().drawType == 2:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start ,self.end)
            self.items.append(self.scene.addRect(rect, pen, brush))       # 빈 리스트에 라인 객체 모두 담음
    # 곡선 그리기
        elif self.parent().drawType == 3:
            line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())   # 현재 선을 추가 
            self.scene.addLine(line, pen)       # 씬에 선 객체 추가       
            self.start = e.pos()        # 끝점을 다시 시작점으로
    # 타원 그리기
        elif self.parent().drawType == 4:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.items.append(self.scene.addEllipse(rect,pen,brush))
    # 지우개 그리기
        elif self.parent().drawType == 5:
            print("dddddddeeeeeeeeeee")
            brush = QBrush(QColor(255,255,255))
            print(brush)
            pen = QPen(QColor(255,255,255),1)
            rect = QRectF(self.start, self.end)
            self.items.append(self.scene.addRect(rect, pen, brush))

    def mouseReleaseEvent(self,e):
        # print('마우스를 뗄 때')
        self.end = e.pos()
        pen = QPen(self.parent().pencolor,self.parent().combo.currentIndex()+1)    # 펜 객체 만듦

        if self.parent().drawType == 1:        
            line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())   # 현재 선을 추가
            self.scene.addLine(line, pen)       
            # print(self.items)       
        elif self.parent().drawType == 2:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start ,self.end)
            self.scene.addRect(rect, pen, brush)       # 빈 리스트에 라인 객체 모두 담음
        elif self.parent().drawType == 4:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.scene.addEllipse(rect,pen,brush)
        elif self.parent().drawType == 5:
            print("dddddddddddddddddd")
            brush = QBrush(QColor(255,255,255))
            pen = QPen(QColor(255,255,255),1)
            rect = QRectF(self.start, self.end)
            self.scene.addRect(rect, pen, brush)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())
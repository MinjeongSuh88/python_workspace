import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):       # QWidget 상속 받은 MyApp 클래스
    def __init__(self):     # 초기화 함수
        super().__init__()  # 부모꺼 상속
        self.initUI()       # 인스턴스 함수 실행

    def initUI(self):       
        self.setGeometry(100,100,1000,800)      # 100,100 위치에 1000,800 짜리 창 만듦
    # 전체 폼
        frmbox = QHBoxLayout()      # 전체 수평 박스 객체 만듦
        self.setLayout(frmbox)      # 현재창에 frmbox 레이아웃 적용

    # 좌측 레이아웃
        leftbox = QVBoxLayout()     # 왼쪽용 수직 박스 객체 만듦
        rightbox = QVBoxLayout()    # 오른쪽용 수직 박스 객체 만듦   

    # 좌측 레이아웃
        gb = QGroupBox('타입')      # 그룹 박스 객체 만듦
        leftbox.addWidget(gb)       # 왼쪽용 수직 박스에 그룹 박스 객체 추가

        box1 = QVBoxLayout()        # 수직 박스 객체 만듦
        gb.setLayout(box1)          # 그룹 박스 객체에 수직 박스 레이아웃 적용

        self.rbtnLine = QRadioButton('직선',self)       # 라디오 버튼 객체 생성
        self.rbtnRect = QRadioButton('사각형',self)
        self.rbtnCurve = QRadioButton('곡선',self)
        self.rbtnEllipse = QRadioButton('타원',self)
        
        box1.addWidget(self.rbtnLine)       # 수직 박스에 직선 라디오 버튼 위젯 추가 
        box1.addWidget(self.rbtnRect)       # 추가한 라디오 버튼 위젯들이 차례대로 위치함
        box1.addWidget(self.rbtnCurve)      
        box1.addWidget(self.rbtnEllipse)

        self.rbtnLine.clicked.connect(self.radioBtnClicked)     # 라디오 버튼을 클릭하면 해당 함수로 연결하는 이벤트 작성
        self.rbtnRect.clicked.connect(self.radioBtnClicked)
        self.rbtnCurve.clicked.connect(self.radioBtnClicked)
        self.rbtnEllipse.clicked.connect(self.radioBtnClicked)

        self.rbtnLine.setChecked(True)      # 기본으로 직선 라디오버튼에 체크되어져 있도록 설정
        self.drawType = 1       # 초기값 설정 - 1. 직선, 2. 사각형                   


    # 그룹박스2
        gb2 = QGroupBox('Pen setting')      # 그룹 박스 객체2 만듦
        leftbox.addWidget(gb2)      # 왼쪽용 수직 박스에 그룹 박스 객체2 추가

        grid = QGridLayout()        # 그리드 객체 만듦
        gb2.setLayout(grid)         # 그룹 박스 객체2에 그리드 레이아웃 형식 적용

        label = QLabel('선굵기')        # 레이블 객체 만듦
        grid.addWidget(label,0,0)       # 그리드 객체 0행 0열에 레이블 위젯 추가

        self.combo = QComboBox()        # 콤보 객체 만듦, self를 붙여서 인스턴스 변수가 됨
        grid.addWidget(self.combo,0,1)      # 그리드 객체 0행 1열에 콤보 위젯 추가
        for i in range(1,21):
            self.combo.addItem(str(i))      # 콤보에 1부터 20까지 번호를 아이템으로 추가

        label2 = QLabel('선색')     # 레이블 객체 만듦
        grid.addWidget(label2,1,0)      # 그리드 객체 1행 0열에 레이블 위젯 추가

    # 펜 색상
        self.pencolor = QColor(0,0,0)       # rgb형식을 지정한 컬러 객체 생성, self를 붙여서 전역변수 됨
        self.penbtn = QPushButton()     # 버튼 객체 만듦
        self.penbtn.setStyleSheet('background-color:rgb(0,0,0)')        # 버튼 객체의 배경색을 css형식으로 컬러 지정
        grid.addWidget(self.penbtn,1,1)     # 그리드 객체 1행 1열에 버튼 객체 추가

        self.penbtn.clicked.connect(self.selectColorDialog)     # 색상 선택 버튼 클릭하면 팔레트 함수 실행

    # 그룹 박스 3
    # 붓 설정
        gb3 = QGroupBox('붓 설정')      # 그룹 박스 객체 만듦
        leftbox.addWidget(gb3)      # 왼쪽용 수직 박스에 그룹 박스 객체3 추가

        hbox = QHBoxLayout()        # 수평 박스 객체 만듦
        gb3.setLayout(hbox)     # 그룹 박스 객체3에 수평 박스 레이아웃 적용

        label3 = QLabel('붓 색상')      # 레이블 객체 만듦
        hbox.addWidget(label3)      # 수평 박스 객체에 레이블 객체 추가

        self.brushcolor = QColor(255,255,255)       # rbg형식을 지정한 컬러 객체 생성, self를 붙여서 전역변수 됨
        self.brushbtn = QPushButton()       # 버튼 객체 생성
        self.brushbtn.setStyleSheet('background-color:rgb(255,255,255)')        # 버튼 객체의 배경색을 css형식으로 컬러 지정
        hbox.addWidget(self.brushbtn)       # 수평 박스 객체에 버튼 객체 추가

        self.brushbtn.clicked.connect(self.selectColorDialog)       # 붓색상 선택 버튼 클릭하면 팔레트 함수롱 연결하는 이벤트

    # 그룹 박스 4
    # 지우개 - 사각 지우개, 올 클리어
        gb4 = QGroupBox('지우개')       # 그룹 박스 객체4 만듦
        leftbox.addWidget(gb4)      # 왼쪽용 수직 박스 객체에 그룹 박스 객체 추가

        hbox4 = QVBoxLayout()       # 수직 박스 객체4 만듦
        gb4.setLayout(hbox4)        # 그룹 박스 객체4에 수직 박스 레이아웃 적용

        self.ers = QPushButton('지우기',self)       # 버튼 객체 만듦
        self.ersa = QPushButton('리셋',self)        # 버튼 객체 만듦
        hbox4.addWidget(self.ers)       # 수직 박스 객체4에 버튼 객체 추가
        self.ers.clicked.connect(self.erase)       #  버튼 객체를 클릭하면 해당 함수로 연결하는 이벤트 
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
        img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))       # 현재 뷰에서 씬을 사각형 모양으로 잡아서 이미지 객체로 만듦 
        # print(img)
        # img.save('e:/data.png')       # 2줄로 파일이 고정 위치, 명으로저장됨
    # 파일 선택헤서 이 이미지 저장할 수?
        fname = QFileDialog.getSaveFileName(self,'어따 저장할래?','./')     # 파일명.확장자까지 정해줘야 함, ./ :현재 디렉토리 기준으로 저장하는 다이얼로그 창 뜸
        print(fname)        # ('C:/Users/user/Desktop/asdf.png', 'All Files (*)') :튜플 형식으로 정보를 갖고 있음
        if fname[0]:        # ==1 을 줄여서 쓴 것 = 파일명이 존재하면, 0이면 존재하지 않는다는 뜻
            img.save(fname[0])      # fname 안에 .이 없으면 확장자가 지정되지 않았다는 것이기 때문에 +'.png'로 무조건 지정해줘도 됨
         
    def erase(self):        # 지우기 버튼을 누르면 실행되는 이벤트 핸들러
        self.drawType = 5       # 드로우타입 변수에 5값을 대입시킴
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
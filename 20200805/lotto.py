import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('로또 번호 추출기')
        # self.setGeometry(100,100,1000,500)

        frmbox = QVBoxLayout()
        self.setLayout(frmbox)
        
        tbox = QHBoxLayout()
        btbox = QHBoxLayout()
        
        q_img = QPixmap('./img/lotto/q.jpg')
        self.n1 = QLabel('1',self)
        self.n1.setPixmap(q_img)
        tbox.addWidget(self.n1)
        
        self.n2 = QLabel('2',self)
        self.n2.setPixmap(q_img)
        tbox.addWidget(self.n2)

        self.n3 = QLabel('3',self)
        self.n3.setPixmap(q_img)
        tbox.addWidget(self.n3)
        
        self.n4 = QLabel('4',self)
        self.n4.setPixmap(q_img)
        tbox.addWidget(self.n4)
        
        self.n5 = QLabel('5',self)
        self.n5.setPixmap(q_img)
        tbox.addWidget(self.n5)
        
        self.n6 = QLabel('6',self)
        self.n6.setPixmap(q_img)
        tbox.addWidget(self.n6)
        
        self.btn = QPushButton('두구두구!!',self)
        self.btn.clicked.connect(self.getLotto)
        btbox.addWidget(self.btn)

        self.show()

        frmbox.addLayout(tbox)
        frmbox.addLayout(btbox)

    def getLotto(self):
        lotto=[]
        i = 0
        while i < 6: # 6자리가 모두 완성되면
            r = random.randint(1,45)
            if r in lotto: # 중복된 값이 있으면 다시 뽑음
                continue
            else:
                lotto.append(r) # lotto 리스트에 담음
                i += 1
        print(lotto)
    
        self.n1.setPixmap(QPixmap('./img/lotto/ball'+str(lotto[0])+'.png'))
        self.n2.setPixmap(QPixmap('./img/lotto/ball'+str(lotto[1])+'.png'))
        self.n3.setPixmap(QPixmap('./img/lotto/ball'+str(lotto[2])+'.png'))
        self.n4.setPixmap(QPixmap('./img/lotto/ball'+str(lotto[3])+'.png'))
        self.n5.setPixmap(QPixmap('./img/lotto/ball'+str(lotto[4])+'.png'))
        self.n6.setPixmap(QPixmap('./img/lotto/ball'+str(lotto[5])+'.png'))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())
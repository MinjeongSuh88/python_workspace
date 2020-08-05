import turtle as t # turtle이라는 외부 툴을 가져와서 사용, 약어 t로 사용
t.shape('turtle') # 펜의 모양 
t.color('pink') # 펜의 컬러
for i in range(4): # 앞으로 100, 오른쪽으로 90도 꺽는 것을 4번 반복
    t.forward(100) 
    t.right(90)


t2=t.Pen() # 펜 기능을 t2에 부여
t2.shape('turtle')
t2.color('red')
t2.penup() # 펜을 듬
t2.goto(-200,100) # 펜을 해당 좌표로 이동
t2.pendown()
t2.begin_fill()
t2.fillcolor('orange')
t2.circle(25) # 반지름 기준으로 원을 그림
t2.end_fill()


t3=t.Pen()
t3.shape('turtle')
t3.shapesize(5)
t3.color('blue')
t3.penup()
t3.goto(100,100)
t3.pendown()
for i in range(5):
    t3.fd(100)
    t3.right(72)


t4=t.Pen()
t4.shape('turtle')    
t4.penup()
t4.goto(200,100)
t4.pendown()
t4.circle(50,200) # 반지름,  각도


t.mainloop() # 창 안 닫히고 놔둠


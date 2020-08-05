import turtle as t # turtle이라는 외부 툴을 가져와서 사용, 약어 t로 사용
t.shape('turtle') # 펜의 모양 
t.color('black') 

t.circle(150)

# 입 왼쪽
t.penup()
t.goto(0,50)
t.pendown()
t.circle(100,-50) # 반지름 100짜리를, 반대 방향으로 50 정도만 그림

# 입 오른쪽
t.penup()
t.goto(0,50)
t.left(45)
t.pendown()
t.circle(100,50)

# 오른쪽 눈
t.penup()
t.goto(85,150)
t.pendown()
t.circle(35)

# 오른쪽 눈알
t.penup()
t.goto(70,170)
t.pendown()
t.begin_fill()
t.fillcolor('black')
t.circle(10)
t.end_fill()

# 왼쪽 눈
t.penup()
t.goto(-50,150)
t.pendown()
t.circle(35)

# 왼쪽 눈알
t.penup()
t.goto(-65,170)
t.pendown()
t.begin_fill()
t.fillcolor('black')
t.circle(10)
t.end_fill()

# 오른쪽 이빨
t.penup()
t.goto(5,50)
t.pendown()
t.begin_fill()
t.right(135)
t.forward(30)
t.left(90)
t.forward(35)
t.left(90)
t.forward(38)
t.end_fill()

# 왼쪽 이빨
t.penup()
t.goto(-5,50)
t.pendown()
t.begin_fill()
t.right(180)
t.forward(30)
t.right(90)
t.forward(35)
t.right(90)
t.forward(40)
t.end_fill()

t.mainloop()
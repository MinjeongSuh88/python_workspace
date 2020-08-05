from turtle import *
import random

a = Turtle() # 그림 그리는 커서
screen = Screen() # 그림판
print(a)
print(screen)

screen.addshape('audience.gif') # 그림 삽입
screen.addshape('turtle.gif') # 그림 삽입
a.shape('audience.gif') #  거북이 커서 모양을 그림으로 바꿈
a.penup()
a.goto(0,260)
# while True:
#     i = random.randint(200,260)
#     a.goto(0,i)

p = Turtle()
p.speed(8)
p.right(90)
p.penup()
p.goto(-350,40)
for i in range(1,6):
    p.pendown()
    p.write(str(i*100)+'m')
    p.fd(280)
    p.penup()
    p.back(280) #bk =backward
    p.left(90)
    p.fd(150)
    p.right(90)
p.goto(1000,1000)    

t1 = Turtle()
t1.shape('turtle')
t1.color('red')
t1.penup()
t1.goto(-400,0)
t1.pendown()
t1.write('1번 꼬북')

t2 = Turtle()
t2.shape('turtle')
t2.color('orange')
t2.penup()
t2.goto(-400,-50)
t2.pendown()
t2.write('2번 꼬북')

t3 = Turtle()
t3.shape('turtle')
t3.color('green')
t3.penup()
t3.goto(-400,-100)
t3.pendown()
t3.write('3번 꼬북')

t4 = Turtle()
t4.shape('turtle')
t4.color('blue')
t4.penup()
t4.goto(-400,-150)
t4.pendown()
t4.write('4번 꼬북')    

t5 = Turtle()
t5.shape('turtle')
t5.color('purple')
t5.penup()
t5.goto(-400,-200)
t5.pendown()
t5.write('5번 꼬북')

n = textinput('골라','어떤 거북이에게 응원하실건가요?')
a.color('red')
a.write(n+'번 꼬부기 이겨라....',left)

dis1 = 0
dis2 = 0
dis3 = 0
dis4 = 0
dis5 = 0

for i in range(125):
    rnd1 = random.randint(1,10)
    rnd2 = random.randint(1,10)
    rnd3 = random.randint(1,10)
    rnd4 = random.randint(1,10)
    rnd5 = random.randint(1,10)
    dis1 += rnd1
    dis2 += rnd2
    dis3 += rnd3
    dis4 += rnd4
    dis5 += rnd5
    t1.fd(rnd1)
    t2.fd(rnd2)
    t3.fd(rnd3)
    t4.fd(rnd4)
    t5.fd(rnd5)
    if (dis1 >= 650):
        t1.penup()
        t1.goto(0,100)
        t1.pendown()
        t1.shape('turtle.gif')
        break
    elif (dis2 >= 650):
        t2.penup()
        t2.goto(0,100)
        t2.pendown()
        t2.shape('turtle.gif')
        break
    elif (dis3 >= 650):
        t3.penup()
        t3.goto(0,100)
        t3.pendown()
        t3.shape('turtle.gif')
        break
    elif (dis4 >= 650):
        t4.penup()
        t4.goto(0,100)
        t4.pendown()
        t4.shape('turtle.gif')
        break
    elif (dis5 >= 650):
        t5.penup()
        t5.goto(0,100)
        t5.pendown()
        t5.shape('turtle.gif')
        break
t1.write(dis1)
t2.write(dis2)
t3.write(dis3)
t4.write(dis4)
t5.write(dis5)

mainloop() # 그림판에 계속 되도록

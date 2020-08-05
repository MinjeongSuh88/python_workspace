import turtle as t

t.color('red')
t.shape('turtle')
t.shapesize(1)
# t.delay(20) # 속도 느리게
t.speed(9)
t.fd(100) # forward의 줄인 표시
dis = 100
rad = 90
for i in range(100):
    dis += 5
    rad += 2 
    t.rt(rad)
    t.fd(dis) # 2씩 늘린 변수를 대입시켜 각도를 늘림

t.mainloop()
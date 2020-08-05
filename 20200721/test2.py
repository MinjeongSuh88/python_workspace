from turtle import * # 약자를 따로 지정하지 않아도 모두 turtle 작업 됨

name = textinput('이름','당신의 이름을 입력하세요') # 팝업창 띄움(타이틀, 내용)
print(name)
shape('turtle')
color('#ff6600')

# def 이름():   -> 함수 :몇 개의 명령들을 모아서 이름 부여해놓은 것 -> 자주 사용하는 기능을 함수로 define
#     처리할 문장
def w(): # w라는 함수는 앞으로 50 전진하는 것으로 명명
    fd(50)
def d(): # d라는 함수는 오른쪽으로 90도 꺽은 후 앞으로 50 전진하는 것으로 명명
    rt(90)    
    fd(50)
def a(): # a라는 함수는 왼쪽으로 90도 꺽은 후 앞으로 50 전진하는 것으로 명명
    lt(90) # 왼쪽
    fd(50)
def s(): # s라는 함수는 반대로 꺽은 후 앞으로 50 전진하는 것으로 명명
    lt(180)
    fd(50)

onkey(w,"w") # onkey :함수와 키를 연결
onkey(d,"d") # a,s,d,w를 방향키로 지정
onkey(a,"a")
onkey(s,"s")

listen() # 내가 입력하는지를 듣는 기능

mainloop()
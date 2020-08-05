def do_test(x,y):
    print("x :",x)
    print("y :",y)
    print('x-y :',x-y)
do_test(100,200) # 매개변수가 여러개일 때 값을 대입하는 순서가 중요함
do_test(y=100,x=200) # 많거나 헷갈릴 때 변수를 사용해서 구체적으로 지정


def do_test(*k): # 가변인수 사용하여 한 번에 받음
    sum = 0
    for i in k:
        sum += i # k안에 있는 요소들을 누적합
        print('i :',i,', sum:',sum)
    return sum # 나를 호출한 애에게 값을 돌려줘
x = do_test(300,100,200,300) # 리턴으로 인하여 돌아온 값을 변수 x에 담음


def do_test1(**kwargs): # ** :딕셔너리(키와 밸류)를 동적으로 받아줌
    for key, val in kwargs.items():
        print('key :',key,', val:',val)
do_test1(name='홍길동',age=20)


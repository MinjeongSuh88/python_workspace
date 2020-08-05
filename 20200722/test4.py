# 이름, 직업, 나이, 사는곳, 키
def show_info(name,job,age,state,height):
    print('이름 :',name,', 직업 :',job,', 나이 :',age,', 사는곳 :',state,', 키 :',height)

show_info('홍길동','도적','20','율도국',180.3)

def show_info1(name,job,age,state,height):
    pass # 아직 어떻게 정의할지 모를 떄
    print('이름 : {0}, 직업 : {1}, 나이 : {2}, 사는곳 : {3}, 키 : {4}'.format(name,job,age,state,height))

show_info1('홍길동','도적','20','율도국',180.3)

p={'name':'홍길동','job':'도적','age':20,'state':'율도국','height':180.3} # 딕셔너리 만듦
print(p)
show_info1(*p) # * 하나 일 때는 key값만 전달
show_info1(**p) # * 두 개 일 떄는 value값만 전달

# def show_info2(name,job,age,state,height):
#     pass # 아직 어떻게 정의할지 모를 떄
#     print('이름 : {0}, 직업 : {1}, 나이 : {2}, 사는곳 : {3}, 키 : {4}'.format(job,name,age,state,height)) # 동적 타이핑
# show_info2('홍길동','도적','20','율도국',180.3)


print('---------------------')
def test(a,b,c):
    print('a :', a)
    print('b :', b)
    print('c :', c)
test(b=20,a=10,c=30) # 순서가 바뀔 걱정없이 다이렉트로 지정


# x 리스트의 요소 합 구하기
x=[10,20,30]
def sumValue(a,b,c):
    return a+b+c
print(sumValue(*x)) # * :변수 x의 값이 하나가 아님을 표시

# def sumValue2(*args):
#     print('b :',b)
# sumValue2(x)

def show_info2(**kwargs): # keyward, arguments
    for kw, arg in kwargs.items():
        print(kw,":",arg,end=" ")
    print()
show_info2(name='홍길동') # 키와 값을 '='을 사용해 쌍으로 묶으면 딕셔너리로 인식이 되어 가변인수에 넣음
show_info2(**p)


def find_birth(birth):
    print(birth[:2]+'년',birth[2:4]+'월',birth[4:6]+'일')
find_birth('880101-1234567') # 88년 1월 1일
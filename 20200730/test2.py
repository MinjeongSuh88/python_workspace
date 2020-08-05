class Car:
    def __init__(self):
        print('초기화 함수')
    
    def __del__(self):
        print('폐차...')

    def __str__(self): # 서용 목적 :문자열화해 반환
        return 'str method가 호출됨'

# 매직함수 : 가장 일반적인 용도로는 오퍼레이터 오버로딩
# + : __add__
# - : __sub__
# * : __mul__
# / : __truediv__
# // : __floordiv__
# % : __mod__
# ** : __pow__
# < : __lt__ (less than)        
# > : __gt__ (greater than)
# > : __ge__ (great equal)

c2 = Car()
print(str(c2))

del c2 # del 소멸자, __init__ 생성자
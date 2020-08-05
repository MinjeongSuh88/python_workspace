def make2(fn):
    def test2():
        return '곤니찌와' + fn()
    return test2
#    return lambda: '곤니찌와' + fn() # 위의 2줄을 매개변수 없는 람다 함수 한 줄로 표현

def make1(fn): # 함수를 매개변수로 받음
#    def test():
#       return '니하오' +fn()
#    return test
    return lambda: '니하오' + fn() # fn() :매개변수 함수를 실행하기 때문에 함수 f1의 매개변수 fn에 그냥 변수가 대입되면 에러

def hello():
    return '한라봉'

print(make2(make1(hello)))
hi = make2(make1(hello)) # hi는 람다함수
print(hi()) # print(make2(make1(hello))()) 와 같음



# 데코레이터(decorator), 다른언어에서는 annotator라고 함
@make2 # 함수 make2에 함수 hello2를 매개변수로 넣은 함수 make1을 매개변수로 넣음
@make1 # 함수 make1에 함수 hello2를 매개변수로 넣음
def hello2():
    return '소망이'

hi = hello2
print(hi()) # print(make2(make1(hello2))())와 같음

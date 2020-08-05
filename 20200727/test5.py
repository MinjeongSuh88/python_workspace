# 임포트 하는 방법 3가지

print('------------------------')
# 1. import 모듈명 -> 모듈채로 가져오기
# import random
# import math

# 2. from 모듈명 import 함수명 -> 다른 모듈에 동명의 함수가 있을 경우 충돌 우려 있음
from random import randint
n = randint(100,200) # 한 개만 불러왔기 때문에 모듈명.이 아니라 단독으로 함수명을 사용할 수 있음
print(n)
print(dir()) # 현재 불러와온 모듈에서 사용할 수 있는 목록들 확인

# 3. from random import * -> 모듈명. 없이 함수명 단독 사용 가능하나 동명의 함수가 있을 경우 충돌 우려 있음
# from random import *
# print(dir())


# 문제 1
def avg(a,b):
    return (a+b)/2
if __name__ == '__main__':
    print(avg(200,100))


# 문제 2
sList = [90,80,23,55,32,50,95,90,85,60,75,35,88,92]
def max_min(listData):
    return max(listData),min(listData)
if __name__ == '__main__':
    print(max_min(sList))
    

# 문제 3
import os 
def get_list(path):
    return os.listdir(path)
if __name__ == '__main__':
    print([i for i in get_list('e:/dev/python_workspace/20200727') if i.endswith('.txt')])


# 문제 4
import time    
def get_todate():
    date = time.ctime().split()    
    return date[1]+'월 '+date[2]+'일'
if __name__ == '__main__':
    print(get_todate())    


# 문제 5
def get_triangle_area(width,height):
    return int(width*height/2)
if __name__ == '__main__':
    print(get_triangle_area(100,200))    


# 문제 6
import math
def get_circle_area(radius):
    return print(math.pi*radius**2)
if __name__ == '__main__':
    print(get_circle_area(10))


# 문제 7
nList=[]
import random as r
for i in range(20):
    nList.append(r.randint(1,100))
if __name__ == '__main__':
    print(nList)    


# 문제 8
def get_odd(list):
    return len([i for i in list if i%2 != 0])
if __name__ == '__main__':
    print(get_odd(nList))


# 문제 9
wordList=[]
char=''
for j in range(20):
    for i in range(5):
        char += chr(r.randint(97,122))
    wordList.append(char)
    char=''
if __name__ == '__main__':
    print(wordList)  


# 문제 10
def get_last_word(list):
    return [i[2:] for i in list]
if __name__ == '__main__':
    print(get_last_word(wordList))


# 문제 11


# 문제 12


# 문제 13


# 문제 14
# 1. import 모듈명
# 2. from 모듈명 import 함수명
# 3. from 모듈명 import *


# 문제 15


# 문제 16
with open('./20200727/rain.txt','r',encoding='utf-8') as kkang:
    print(len([i for i in kkang.read().split() if len(i) == 4]))


# 문제 17
user = input('디렉토리를 입력하시오')
with open('./20200727/dir.txt','w',encoding='utf-8') as file:
    file.writelines(os.listdir(user))


# 문제 18
import random as r
with open('./20200727/lotto.txt','w') as file:
    for i in range(6):
        file.writelines(str(r.randint(1,46))+'\n') # +로 해야 한 단어로 묶이기 때문에 ,사용하면 안 됨
        

# 문제 19
str = ''
with open('./20200727/randomchar.txt','w') as file:
    for i in range(3):
        str += chr(r.randint(97,123))
    file.writelines(str)


# 문제 20
with open('./20200727/stock.txt','r',encoding='utf-8') as file:
    with open('./20200727/stock.csv','w',encoding='utf-8') as file2:
        file2.writelines([i+',' for i in file.read().split()])
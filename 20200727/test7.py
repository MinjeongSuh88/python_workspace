# 파일 입출력
import os
print(os.getcwd()) # 현재 작업 중인 디렉토기 경로 얻어오기

file = open('./20200727/hello.txt','r') # 1. 파일 열기 :open('파일명','모드'), r:read
print(file) 
file.read()
# print(file.read(), type(file.read())) # 2. 읽기
file.close() # 3. 다시 닫음 -> 닫지 안흥면 다른 사용자가 저장을 못 함


print('-------------------------')
file2 = open('./20200727/hello2.txt','w') # 파이썬에서 txt파일을 직접 생성, w:write
print(file2)
file2.write('금요일 같은 월요일이면 좋겟다..') # 문자열 1개만 기록 가능
help(file2.write)
file.close()



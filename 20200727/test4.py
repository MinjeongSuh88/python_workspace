# 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해주는 모듈 :os
import os
# print(dir(os))

print(os.getcwd()) # 현재 작업 디렉토리(current work directory)

print(os.listdir()) # 현재 작업 디렉토리에 있는 파일과 디렉토리 목록 검색

print(os.listdir('20200727')) # 이 파일에 있는 파일 목록 검색
print(os.listdir('.')) # . 현재 디렉토리 -> E:\dev\python_workspace
                       # .. 부모 디렉토리
print(os.listdir('e:\dev\python_workspace')) # 원하는 디렉토리의 주소 직접 입력

print([i for i in os.listdir('20200727')]) # 현재 작업 디렉토리에 있는 모든 파일을 출력
print([file for file in os.listdir('C:\\Users\\user\\Downloads\\') if file.endswith('zip')]) # endswith :파일의 끝 부분이 zip으로 되어 있는지
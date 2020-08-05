# CPU
# intel :CPU 제조사
# X86 :intel이 만든 CPU 제조번호 계열(8086,80286,80386,80486,Pentium)

# 멀티테스크 :작업을 여러개 실행
# CPU :워커, RAM :작업공간
# DB, 웹서비스 등은 멀티 CPU가 효율적

# Thread :하나의 프로세스 내에서 진행되는 하나의 실행 단위를 의미
# Multi Thread :하나의 프로그램 안에서 여러 프로세스 진행(카톡-채팅,파일전송)
# 프로세서 :메모장, 워드, 카톡 등은 각자의 메모리와 실행을 함

# 파이선에서 멀티쓰레드 구현 방법
# 1. 쓰레드가 실행할 함수, 메서드 작성
# 2. Threading.Thread로부터 파생된 파생클래스를 작성하여 사용하는 방식

import threading

def run(who):
    for i in range(1,101):
        print(str(i)+'미터 달리는 중', who)

# run('번개')
# run('천둥')
# 멀티 쓰레드 처리
t1 = threading.Thread(target = run, args = ('번개',))
t2 = threading.Thread(target = run, args = ('천둥',))

# start() :쓰레드 동작시킨다.
t1.start() 
t2.start()

print('main Thread end....................')

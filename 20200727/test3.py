import time # 시간과 연관있는 모듈

# help(time)
print(time.time()) 
print(time.ctime(),type(time.ctime())) # time.ctime() :현재 시간-요일,월,일,시간,년도가 스페이스 바로 구분

print(time.ctime().split())
print(time.ctime().split()[4])
print(time.ctime().split()[-1])

print(dir(time)) # time 모듈 안에 있는 함수들 조회

# 지금 시간을 1초에 한 번씩 출력
# while True:
#     time.sleep(1) # 일하는 프로세스에게 1초만 자
#     print(time.ctime()) 


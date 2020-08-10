import pygame
import random as r

pygame.init()       # 사용 전 꼭 초기화해야 함

pygame.display.set_caption('토끼 사냥')     # 게임 제목

# 배경 화면 그리기 준비
screen_width = 1200     # 창 너비 변수
screen_height = 800     # 창 높이 변수
screen = pygame.display.set_mode((screen_width,screen_height))      # 화면 객체 생성, set_mode 함수는 매개변수를 튜플 형식으로 넣음
bg = pygame.image.load('e:/dev/python_workspace/img/bg.jpg')        # 게임 배경 이미지 객체, 실제 크기는 1900*974픽셀

# 토끼 그리기 준비
rb = pygame.image.load('e:/dev/python_workspace/img/rabbit1.png')       # 토끼 이미지 객체
rb2 = pygame.image.load('e:/dev/python_workspace/img/rabbit2.png')      # 토끼 이미지 객체2

rx = 100
ry = 100
cnt = 0
isRunning = True        # flag성 변수 :게임을 계속 진행할지, 중지할지를 결정하는 변수
while isRunning:        # True 대신 flag성 변수 사용
    cnt += 1        # 반복문 돌 때마다 cnt가 1씩 증가 
    for event in pygame.event.get():       # 게임 상의 이벤트 모으기
        if event.type == pygame.QUIT:       # 다양한 이벤트 중 게임 종료가 있으면       
            isRunning = False       # isRunning 변수 값을 False로 바꿈
# 배경 그리기
    screen.blit(bg,(0,0))       # 배경에 이미지 객체 적용
# 토끼 그리기
    # rx = r.randint(0,1000)
    # ry = r.randint(0,700)
    if cnt % 2 == 0:
        screen.blit(rb,(rx,ry))       # 배경 위에 쌓는 개념으로 순서가 있음, 토끼가 움직이도록 위치 좌표를 변수로 둠
    else:
        screen.blit(rb2,(rx,ry))       # 배경 위에 쌓는 개념으로 순서가 있음
    # print(cnt)      # 그림을 계속 그리는 중임을 알 수 있음






    pygame.display.update()     # 게임 화면을 다시 그리기



pygame.quit()
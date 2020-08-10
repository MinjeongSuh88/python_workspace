import pygame
import random as r

pygame.init()       # 사용 전 꼭 초기화해야 함

pygame.display.set_caption('토끼 사냥')     # 게임 제목

# 배경 화면 그리기 준비
screen_width = 1200     # 창 너비 변수
screen_height = 800     # 창 높이 변수
screen = pygame.display.set_mode((screen_width,screen_height))      # 화면 객체 생성, set_mode 함수는 매개변수를 튜플 형식으로 넣음
bg = pygame.image.load('e:/dev/python_workspace/img/bg.jpg')        # 게임 배경 이미지 객체, 실제 크기는 1900*974픽셀
bg2 = pygame.image.load('e:/dev/python_workspace/img/bg.jpg')        #   배경 이동을 위해 게임 배경 이미지 객체 하나 더 생성
bg = pygame.transform.scale(bg,(1200,800))        # 배경 이미지 객체 사이즈 수정
bg2 = pygame.transform.scale(bg2,(1200,800))        # 배경 이미지 객체 사이즈 수정

# 토끼 그리기 준비
rb = pygame.image.load('e:/dev/python_workspace/img/rabbit1.png')       # 토끼 이미지 객체
rb2 = pygame.image.load('e:/dev/python_workspace/img/rabbit2.png')      # 토끼 이미지 객체2
rb = pygame.transform.scale(rb,(75,100))        # 토끼 이미지 객체 사이즈 수정
rb2 = pygame.transform.scale(rb2,(75,100))

# 시계 변수
clock = pygame.time.Clock()

rx = 500        # 토끼 좌표 변수
ry = 300
bgx = 0     # 배경 좌표 변수
bgx2 = 1200
cnt = 0
count = 0
isRunning = True        # flag성 변수 :게임을 계속 진행할지, 중지할지를 결정하는 변수
while isRunning:        # True 대신 flag성 변수 사용
    for event in pygame.event.get():       # 게임 상의 발생하는 모든 이벤트 중에
        if event.type == pygame.QUIT:       # 다양한 이벤트 중 게임 종료가 있으면       
            isRunning = False       # isRunning 변수 값을 False로 바꿈

# FPS 게임? Frame 지정하면 진행 속도를 조절할 수 있기 때문에 토끼가 5번에 한 번 씩 이동하도록 조정 안 해도 됨
    fps = clock.tick(100)        # 화면에 초당 프레임수를 30으로 지정
    # print('fps :',str(clock.get_fps()))     # 프레임이 얼마인지 확인

# 키보드 키로 토끼 움직이기        
    keys = pygame.key.get_pressed()      # 키보드의 모든 키가 눌렸는지(1) 안 눌렸는지(0) 리스트로 만들어 놓음
    # print(keys[pygame.K_LEFT])      # 왼쪽 방향 버튼을 누르면 1이 프린트 됨
    if keys[pygame.K_LEFT] == 1:      # 왼쪽 방향 버튼이 눌리면
        # if count == 5:      # 5번에 한 번씩 움직이도록 지정 -> 속도 느려짐
        rx -= 5     # 토끼의 x좌표가 작아짐 -> 왼쪽으로 이동
        #     count = 0
        # else:
            # count += 1
    if keys[pygame.K_UP] == 1:      # 왼쪽 방향 버튼이 눌리면       * elif가 아니라 if로 바꾸면 대각선 이동 가능
        ry -= 5     # 토끼의 y좌표가 작아짐 -> 위쪽으로 이동
    if keys[pygame.K_RIGHT] == 1:      # 왼쪽 방향 버튼이 눌리면
        rx += 5     # 토끼의 x좌표가 커짐 -> 오른쪽으로 이동
    if keys[pygame.K_DOWN] == 1:      # 왼쪽 방향 버튼이 눌리면
        ry += 5     # 토끼의 y좌표가 커짐 -> 아래쪽으로 이동

    # if event.type == pygame.KEYUP:      # 키보드 키를 눌렀다가 떼는 상황이면
    #     if event.key == pygame.K_LEFT:      # 키보드 키 이벤트가 왼쪽 방향이면
    #         rx -= 5     # 토끼의 x좌표가 작아짐 -> 왼쪽으로 이동
    #     elif event.key == pygame.K_UP:      # 키보드 키 이벤트가 위 방향이면
    #         ry -= 5     # 토끼의 y좌표가 작아짐 -> 위쪽으로 이동
    #     elif event.key == pygame.K_RIGHT:       # 키보드 키 이벤트가 오른쪽 방향이면
    #         rx += 5     # 토끼의 x좌표가 커짐 -> 오른쪽으로 이동
    #     elif event.key == pygame.K_DOWN:        # 키보드 키 이벤트가 아래 방향이면
    #         ry += 5     # 토끼의 y좌표가 커짐 -> 아래쪽으로 이동

# 배경 그리기
    bgx -= 2        # 배경이 움직이는 것처럼 설정하기 위해 x 좌표를 변수로 지정
    bgx2 -= 2
    screen.blit(bg,(bgx,0))       # 배경에 이미지 객체 적용
    screen.blit(bg2,(bgx2,0))       # 배경에 이미지 객체 적용
    if bgx == -1200:
        bgx = 1200
    if bgx2 == -1200:
        bgx2 = 1200

# 토끼 그리기
    cnt += 1        # 반복문 돌 때마다 cnt가 1씩 증가 
    if cnt % 2 == 0:        # cnt가 짝수이면
        screen.blit(rb,(rx,ry))       # 배경 위에 쌓는 개념으로 순서가 있음, 토끼가 움직이도록 위치 좌표를 변수로 둠
    else:       # 홀수이면
        screen.blit(rb2,(rx,ry))       # 배경 위에 쌓는 개념으로 순서가 있음
    # print(cnt)      # 그림을 계속 그리는 중임을 알 수 있음






    pygame.display.update()     # 게임 화면을 다시 그리기



pygame.quit()
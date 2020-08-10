import pygame
import math
import random

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

# 조준경 그리기 준비
sn = pygame.image.load('e:/dev/python_workspace/img/snipe.png')
sn = pygame.transform.scale(sn,(80,80))

# 구멍 그리기 준비
hl = pygame.image.load('e:/dev/python_workspace/img/hole.png')
hl = pygame.transform.scale(hl,(10,10))
holeList = []       # 구멍을 여러개 그리기 위한 빈 리스트 준비

# 배경 음악
# pygame.mixer.music.load('e:/dev/python_workspace/sounds/backsound.mp3')
# pygame.mixer.music.set_volume(1)       # 0.1 ~ 1까지 볼륨 지정 가능
# pygame.mixer.music.play(1)      # 한 번 플레이

# 특정 사운드 객체 
# fr = pygame.mixer.Sound('e:/dev/python_workspace/sounds/fire.wav')
# fr.set_volume(0.2)
# sc = pygame.mixer.Sound('e:/dev/python_workspace/sounds/scream.wav')
# sc.set _volume(0.2)

# 토끼의 중심좌표와 마우스 클릭 위치와의 거리 구하기
def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

# 반동 변수
rebound = 0


# 시계 변수
clock = pygame.time.Clock()

bgx = 0     # 배경이 움직이는 것처럼 설정하기 위해 x 좌표를 변수로 지정
bgx2 = 1200     # 배경2 x좌표 변수
rx = 500        # 토끼 좌표 변수
ry = 300
snx = 300       # 조준경 좌표 변수
sny = 300
hlx = 300       # 구명 좌표 변수
hly = 300
cnt = 0     # 토끼 이미지 홀짝에 따라 바꾸기 위한 변수
# count = 0       # Frame 지정 전 토끼 이동 속도를 제한하기 위한 변수
isRunning = True        # flag성 변수 :게임을 계속 진행할지, 중지할지를 결정하는 변수
while isRunning:        # True 대신 flag성 변수 사용
    for event in pygame.event.get():       # 게임 상의 발생하는 모든 이벤트 중에
        if event.type == pygame.QUIT:       # 다양한 이벤트 중 게임 종료가 있으면       
            isRunning = False       # isRunning 변수 값을 False로 바꿈
        if event.type == pygame.MOUSEBUTTONUP:      # 마우스를 클릭했다가 뗄 때의 이벤트가 발생되면
            # print('마우스 클릭 됨')
            rebound = 100       # 마우스 클릭할 때 반동으로 인해 조준경이 위로 올라감을 표현
            # fr.play()
            hlx, hly = pygame.mouse.get_pos()       # 마우스의 위치를 얻음
            dis = pythagoras(rx+35,ry+55,hlx,hly)       # 피타고라스 함수의 리턴값을 변수에 담음
            # print(dis)
            if dis <= 25:
                print('아..')
            # 토끼로부터의 상대 좌표를 저장 -> 토끼가 움직일 때마다 구멍이 같이 움직이도록 하기 위해
                holeList.append((rx+35-hlx,ry+55-hly))      # 마우스 클릭할 때 토끼 중점과의 거리가 25픽셀 이하이면 발생한 좌표 -> 튜플로 묶어야 좌표세트로 리스트에 추가됨
                # sc.play()     
    # print('홀 리스트 :',holeList)       
                rx = random.randint(1,1100)
                ry = random.randint(1,690)

# 조준경이 마우스 포인터 따라다니기
    # print(pygame.mouse.get_pos())       # 마우스 포인트 실시간 위치 튜플 형식
    snx,sny = pygame.mouse.get_pos()        # 각 좌표를 변수 2개에 담음
    # print(pygame.mouse.get_pressed())       # 마우스 좌측,휠,우측 누를 때 1로 출력, 튜플 형식

# 조준경에 반동줬다가 다시 내려가기
    if rebound > 2:
        rebound -= 2

# 마우스 좌측 버튼 클릭하면 구멍
    # if pygame.mouse.get_pressed()[0] == 1:

# FPS 게임? Frame 지정하면 진행 속도를 조절할 수 있기 때문에 토끼가 5번에 한 번 씩 이동하도록 조정 안 해도 됨
    fps = clock.tick(80)        # 화면에 초당 프레임수를 30으로 지정
    # print('fps :',str(clock.get_fps()))     # 프레임이 얼마인지 확인

# 키보드 키로 토끼 움직이기        
    keys = pygame.key.get_pressed()      # 키보드의 모든 키가 눌렸는지(1) 안 눌렸는지(0) 리스트로 만들어 놓음
    # print(keys[pygame.K_LEFT])      # 왼쪽 방향 버튼을 누르면 1이 프린트 됨
    if keys[pygame.K_LEFT] == 1:      # 왼쪽 방향 버튼이 눌리면
        if rx == 0:     # 토끼가 배경 밖으로 탈출 안하도록 지정
            rx = 0
        else:
        # if count == 5:      # 5번에 한 번씩 움직이도록 지정 -> 속도 느려짐
            rx -= 5     # 토끼의 x좌표가 작아짐 -> 왼쪽으로 이동
        #     count = 0
        # else:
            # count += 1
    if keys[pygame.K_UP] == 1:      # 왼쪽 방향 버튼이 눌리면       * elif가 아니라 if로 바꾸면 대각선 이동 가능
        if ry == 0:
            ry = 0
        else:
            ry -= 5     # 토끼의 y좌표가 작아짐 -> 위쪽으로 이동
    if keys[pygame.K_RIGHT] == 1:      # 왼쪽 방향 버튼이 눌리면
        if rx == 1125:
            rx = 1125
        else:
            rx += 5     # 토끼의 x좌표가 커짐 -> 오른쪽으로 이동
    if keys[pygame.K_DOWN] == 1:      # 왼쪽 방향 버튼이 눌리면
        if ry == 700:
            ry = 700
        else:
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

# 음악 온오프
#     if key[pygame.K_1] == 1:      # 1번 키를 누르면          
#         pygame.mixer.music.stop()     #  음악 중지
#     if key[pygame.K_2] == 1:      # 2번 키를 누르면
#         pygame.mixer.music.play()     # 음악 시작

# 배경 그리기
    bgx -= 2        # 배경 이미지 좌표가 왼쪽으로 2씩 이동        
    bgx2 -= 2       # 배경 이미지2 좌표가 왼쪽으로 2씩 이동
    screen.blit(bg,(bgx,0))       # 배경에 이미지 객체 적용
    screen.blit(bg2,(bgx2,0))       # 배경에 이미지 객체 적용
    if bgx == -1200:        # 배경 이미지가 왼쪽으로 다 빠지면
        bgx = 1200      # 배경 이미지2의 오른쪽으로 이동
    if bgx2 == -1200:       # 배경 이미지2가 왼쪽으로 다 빠지면
        bgx2 = 1200     # 배경 이미지의 오른쪽으로 이동

# 토끼 그리기
    cnt += 1        # 반복문 돌 때마다 cnt가 1씩 증가 
    if cnt % 2 == 0:        # cnt가 짝수이면
        screen.blit(rb,(rx,ry))       # 배경 위에 쌓는 개념으로 순서가 있음, 토끼가 움직이도록 위치 좌표를 변수로 둠
    else:       # 홀수이면
        screen.blit(rb2,(rx,ry))       # 배경 위에 쌓는 개념으로 순서가 있음
    # print(cnt)      # 그림을 계속 그리는 중임을 알 수 있음

# 총구멍 여러개 
    # for i in range(len(holeList)):      # 구멍   
    #     screen.blit(hl,(holeList[i][0]-5,holeList[i][1]-5))
    for x,y in holeList:      # 리스트에 튜플 형식으로 담겨있기 때문에 x,y로 각각 빼올 수 있음 
        screen.blit(hl,(rx+35-x,ry+55-y))
        
# 조준경 그리기
    screen.blit(sn,(snx-40,sny-40-rebound))     # 조준경 이미지가 100*100이므로 반씩 위치 이동, 반동 변수 추가
    



    pygame.display.update()     # 게임 화면을 다시 그리기



pygame.quit()
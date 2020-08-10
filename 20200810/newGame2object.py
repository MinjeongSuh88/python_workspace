import pygame

# 초기화
pygame.init()

screen_width = 600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('우주 전쟁')

# 배경 이미지 객체
bg = pygame.image.load('e:/dev/python_workspace/img/space.jpg')
bg = pygame.transform.scale(bg,(600,900))       # 이미지 사이즈 조정
bg2 = pygame.image.load('e:/dev/python_workspace/img/space.jpg')
bg2 = pygame.transform.scale(bg,(600,900))       # 이미지 사이즈 조정

# 비행기 이미지 객체
ply = pygame.image.load('e:/dev/python_workspace/img/player1.png')
ply2 = pygame.image.load('e:/dev/python_workspace/img/player2.png')
ply3 = pygame.image.load('e:/dev/python_workspace/img/player3.png')
ply4 = pygame.image.load('e:/dev/python_workspace/img/player4.png')

cnt = 0
bgy = 0
bg2y = -900

# 시계 변수
clock = pygame.time.Clock()
isRunning = True
# 여기 사이의 코드가 반복
while isRunning:
    for event in pygame.event.get():        # 현재 파이게임의 이벤트를 모두 가져와서 하나 씩 꺼냄
        if event.type == pygame.QUIT:       # 창의 x버튼을 누르면 창이 꺼짐
            isRunning = False
    
    # 배경 그리기
    bgy += 2
    bg2y += 2
    screen.blit(bg,(0,bgy))
    screen.blit(bg2,(0,bg2y))
    if bgy == 900:
        bgy = -900
    if bg2y == 900:
        bg2y = -900
    
    # frame 지정
    fps = clock.tick(30)        # 화면에 초당 프레임수 30
    print('fps :',str(clock.get_fps()))
    
    # 비행기 그리기
    cnt += 1
    if cnt % 4 == 0:
        screen.blit(ply,(100,700))
    elif cnt % 4 == 1:
        screen.blit(ply2,(100,700))
    elif cnt % 4 == 2:
        screen.blit(ply3,(100,700))
    elif cnt % 4 == 3:
        screen.blit(ply4,(100,700))

    pygame.display.update()



pygame.quit()
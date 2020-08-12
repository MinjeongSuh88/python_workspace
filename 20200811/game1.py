import pygame
import random

pygame.init()       # 파이게임 초기화

screen_width = 1200     # 너비 변수        
screen_height = 800     # 높이 변수
screen = pygame.display.set_mode((screen_width,screen_height))      # 창 설정
pygame.display.set_caption('핑퐁')      # 창의 제목 지정

# 배경 이미지 객체
bg = pygame.image.load('e:/dev/python_workspace/img/bg.jpg')        # 배경 이미지 객체 생성
bg = pygame.transform.scale(bg,(1200,800))      # 배경 이미지 크기 변경

# 동전 이미지 객체
gd = pygame.image.load('e:/dev/python_workspace/img/gold.png')      # 동전 이미지 객체 생성
gd = pygame.transform.scale(gd,(70,70))     # 동전 이미지 크기 변경
gdx = 600       # 동전 x좌표
gdy = 400       # 동전 y좌표
inc_x = random.randint(-10,10)      # x좌표의 증가값
inc_y = random.randint(-10,10)      # y좌표의 증가값

def changeDirection(x,y,ix,iy):     # 동전이 벽이 부딪히면 진행 방향이 반대로 바뀌게 하는 함수
# 화면 위, 아래쪽 벽에 맞으면 튕겨나가게 설정
    if gdy <= 3 or gdy >= (800-50-3):       # 동전 y좌표가 화면의 위 또는 아래 경계선에 부딪히면
        iy = -iy        # y좌표의 증감을 바꿈
# 화면 왼, 오른쪽 벽에 맞으면 
    if gdx <= 3 or gdx >= (1200-50-3):      # 동전 x좌표가 화면의 왼 또는 오른 경계선에 부딪히면
        ix = -ix        # x좌표의 증감을 바꿈
    return ix, iy       # x, y좌표의 증감을 리턴함

# 시계변수
clock = pygame.time.Clock()

isRunning = True        # 반복 여부 변수
while isRunning:        # 참 동안 반복
    fps = clock.tick(30)        # 1초당 frame수 30으로 지정
    for event in pygame.event.get():        # 게임에서 일어나는 모든 이벤트를 가져와서 그 중
        if event.type == pygame.QUIT:       # 게임을 종료하는 타입이면
            isRunning = False               # 반복 종료

    screen.blit(bg,(0,0))       # 배경 이미지 그림

    gdx -= inc_x        # 동전의 x좌표 점점 감소
    gdy -= inc_y        # 동전 y좌표의 
    screen.blit(gd,(gdx,gdy))       # 동전 이미지 그림
    
    inc_x,inc_y = changeDirection(gdx,gdy,inc_x,inc_y)      # 함수의 리턴값을 두 변수에 각각 담음

    pygame.display.update()     # 디스플레이를 계속 업데이트

pygame.quit()       # 게임 
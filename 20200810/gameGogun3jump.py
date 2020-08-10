import pygame
import random as r
import time
import math

pygame.init()

pygame.display.set_caption('고군분투')

# 배경 객체 
screen = pygame.display.set_mode((800,500))     # 스크린 준비
bg = pygame.image.load('e:/dev/python_workspace/img/bg1.jpg')       # 배경용 이미지 객체
bg2 = pygame.image.load('e:/dev/python_workspace/img/bg2.jpg')      # 화면 반복용으로 같은 이미지 객체

# 캐릭터 객체
ct1 = pygame.image.load('e:/dev/python_workspace/img/run1.png')     
ct2 = pygame.image.load('e:/dev/python_workspace/img/run2.png')
ct3 = pygame.image.load('e:/dev/python_workspace/img/run3.png')
ct4 = pygame.image.load('e:/dev/python_workspace/img/run2.png')

# 동전 객체
gd = pygame.image.load('e:/dev/python_workspace/img/gold.png')
sv = pygame.image.load('e:/dev/python_workspace/img/silver.png')
coinList = []       # 동전 좌표 쌓아둘 리스트
 
class Coin:     # 동전 인스턴스 찍어내는 클래스
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __del__(self):      
        pass

def makeCoin():
    c = Coin(800,gdy[r.randint(0,1)])
    coinList.append(c)

def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    
def collision(x1,y1,x2,y2):
    dis = pythagoras(x1,y1,x2,y2)
    result = 0
    if dis < 50:
        result = 1
    return result

# 시계 변수
clock = pygame.time.Clock()

# 동작
bgx = 0
bg2x = 800
ctx = 270
cty = 270
gdx = 800
gdy = [295,195]
svx = 800
svy = r.randint(150,500)
print(svy)
cnt = 0
sog = 1
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
# 그리기 속도
    fps = clock.tick(70)

# 배경 그리기
    bgx -= 4
    bg2x -= 4
    screen.blit(bg,(bgx,0))
    screen.blit(bg2,(bg2x,0))
    if bgx == -800:
        bgx = 800
    if bg2x == -800:
        bg2x = 800

# 캐릭터 그리기
    if cnt % 4 == 0:
        screen.blit(ct1,(ctx,cty))
    if cnt % 4 == 1:    
        screen.blit(ct2,(ctx,cty))
    if cnt % 4 == 2:    
        screen.blit(ct3,(ctx,cty))
    if cnt % 4 == 3:    
        screen.blit(ct4,(ctx,cty))
    cnt += 1
    print(cnt)

# 동전 그리기
    if cnt % 10 == 0:       # 10번 돌아갈 때 1번 씩
        makeCoin()          # 코인 객체 생성
    for c in coinList:      # 코인 좌표 리스트에서 
        if sog == 1: 
            screen.blit(sv,(c.x,c.y))
            if cnt > 300:
                cnt = 0
                sog = 2
        elif sog == 2:
            screen.blit(gd,(c.x,c.y))
            if cnt > 300:
                cnt = 0
                sog = 1
        c.x -= 4 

    for c in coinList:
        result = collision(ctx,cty,c.x,c.y)
        if result == 1:
            coinList.remove(c)
            del(c)

# 키보드 조작
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] == 1:
        if cty == 0:
            cty = 0
        else:
            cty -= 5
    if keys[pygame.K_DOWN] == 1:
        if cty == 390:
            cty = 390
        else:
            cty += 5
    if keys[pygame.K_SPACE] == 1:
        if 100 <= cty <= 300:
            cty-=10
    if keys[pygame.K_SPACE] == 0:  
        if cty == 270:
            cty = 270
        elif cty < 270 :
            cty += 10

    pygame.display.update()

pygame.quit()
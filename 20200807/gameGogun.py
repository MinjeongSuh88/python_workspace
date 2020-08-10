import pygame
import random as r

pygame.init()

pygame.display.set_caption('고군분투')

# 배경 객체 
screen = pygame.display.set_mode((800,500))
bg = pygame.image.load('e:/dev/python_workspace/img/bg1.jpg')
bg2 = pygame.image.load('e:/dev/python_workspace/img/bg2.jpg')

# 캐릭터 객체
ct1 = pygame.image.load('e:/dev/python_workspace/img/run1.png')
ct2 = pygame.image.load('e:/dev/python_workspace/img/run2.png')
ct3 = pygame.image.load('e:/dev/python_workspace/img/run3.png')
ct4 = pygame.image.load('e:/dev/python_workspace/img/run2.png')

# 동전 객체
gd = pygame.image.load('e:/dev/python_workspace/img/gold.png')
sv = pygame.image.load('e:/dev/python_workspace/img/silver.png')
 
# 시계 변수
clock = pygame.time.Clock()

# 동작
bgx = 0
bg2x = 800
ctx = 350
cty = 390
gdx = 800
gdy = r.randint(150,500)
print(gdy)
svx = 800
svy = r.randint(150,500)
print(svy)
cnt = 0
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

# 동전 그리기
    gdx -= 4 
    screen.blit(gd,(gdx,gdy))
    if gdx <= -854:
        gdx = 800
        gdy = r.randint(150,500)
    svx -= 4 
    screen.blit(sv,(svx,svy))
    if svx <= -854:
        svx = 800
        svy = r.randint(150,500)
            


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
        for i in range(5):
            ctx += 2
            cty += 2
            time.sleep()
        for i in range(5):
            ctx += 2
            cty -= 2


    pygame.display.update()

pygame.quit()
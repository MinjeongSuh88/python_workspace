import pygame

# 초기화
pygame.init()

screen_width = 600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))

isRunning = True

pygame.display.set_caption('우주 전쟁')

# 여기 사이의 코드가 반복
while isRunning:
    for event in pygame.event.get():        # 현재 파이게임의 이벤트를 모두 가져와서 하나 씩 꺼냄
        if event.type == pygame.QUIT:       # 창의 x버튼을 누르면 창이 꺼짐
            isRunning = False
    pygame.display.update()



pygame.quit()
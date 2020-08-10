import pygame

# 초기화
pygame.init()

screen_width = 600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('우주 전쟁')     # 게임 창 제목

# 배경 이미지 객체
bg = pygame.image.load('e:/dev/python_workspace/img/space.jpg')
bg = pygame.transform.scale(bg,(600,900))       # 이미지 사이즈 조정
bg2 = pygame.image.load('e:/dev/python_workspace/img/space.jpg')
bg2 = pygame.transform.scale(bg,(600,900))       # 이미지 사이즈 조정

# 배경 이미지 좌표 변수
bgy = 0
bg2y = -900

# 비행기 이미지 객체
ply = pygame.image.load('e:/dev/python_workspace/img/player1.png')
ply2 = pygame.image.load('e:/dev/python_workspace/img/player2.png')
ply3 = pygame.image.load('e:/dev/python_workspace/img/player3.png')
ply4 = pygame.image.load('e:/dev/python_workspace/img/player4.png')
ply = pygame.transform.scale(ply,(50,50))
ply2 = pygame.transform.scale(ply2,(50,50))
ply3 = pygame.transform.scale(ply3,(50,50))
ply4 = pygame.transform.scale(ply4,(50,50))

# 비행기 우주선 좌표 변수
px = 250
py = 800

# 미사일 객체
missile = pygame.image.load('e:/dev/python_workspace/img/missile1.png')

# 미사일 객체 좌표 변수
mx = 300
my = 500
mxy = []

class Missile:      # 미사일 클래스 선언
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __del__(self):
        # print('소멸자... 미사일 제거됨')
        pass

# 시계 변수
clock = pygame.time.Clock()

cnt = 0
isRunning = True
# 여기 사이의 코드가 반복
while isRunning:
    for event in pygame.event.get():        # 현재 파이게임의 이벤트를 모두 가져와서 하나 씩 꺼냄
        if event.type == pygame.QUIT:       # 창의 x버튼을 누르면 창이 꺼짐
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('마우스 클릭 됨')
            mx, my = pygame.mouse.get_pos()
            mxy.append(Missile(mx,my))      # Missile 클래스 
            # print(mxy)

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
    # print('fps :',str(clock.get_fps()))       # 29.대로 출력
    
    # 마우스 좌표 구하기
    px, py = pygame.mouse.get_pos() 

    # 비행기 그리기
    cnt += 1
    if cnt % 4 == 0:
        screen.blit(ply,(px-25,py-25))      # 비행기의 중앙에 마우스 포인트가 움직이도록 조정
    elif cnt % 4 == 1:
        screen.blit(ply2,(px-25,py-25))
    elif cnt % 4 == 2:
        screen.blit(ply3,(px-25,py-25))
    elif cnt % 4 == 3:
        screen.blit(ply4,(px-25,py-25))

    # 미사일 그리기
    for m in mxy:
        screen.blit(missile,(m.x,m.y-35))
        m.y -= 5
        if m.y < -19:
            mxy.remove(m)     # 리스트 상에서 없어짐
            del(m)      # 아예 메모리 상에서 사라짐
    pygame.display.update()



pygame.quit()
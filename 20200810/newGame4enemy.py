import pygame
import math
import random 

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

# 우주선 플레이어 이미지 객체
ply = pygame.image.load('e:/dev/python_workspace/img/player1.png')      
ply2 = pygame.image.load('e:/dev/python_workspace/img/player2.png')
ply3 = pygame.image.load('e:/dev/python_workspace/img/player3.png')
ply4 = pygame.image.load('e:/dev/python_workspace/img/player4.png')
ply = pygame.transform.scale(ply,(50,50))
ply2 = pygame.transform.scale(ply2,(50,50))
ply3 = pygame.transform.scale(ply3,(50,50))
ply4 = pygame.transform.scale(ply4,(50,50))

# 우주선 플레이어 좌표 변수
px = 250
py = 800

# 미사일 객체
missile = pygame.image.load('e:/dev/python_workspace/img/missile1.png')

# 미사일 객체 좌표 변수
mx = 300
my = 500
mxy = []

class Missile:      # 미사일 클래스 선언
    def __init__(self,x,y):     # x, y좌표를 가지고 있음
        self.x = x
        self.y = y
    
    def __del__(self):
        # print('소멸자... 미사일 제거됨')
        pass

# 미사일과 충돌 테스트
def pythagoras(x1,y1,x2,y2):        
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

# 적우주선 이미지 객체
enm = pygame.image.load('e:/dev/python_workspace/img/gunship0.png')
enm2 = pygame.image.load('e:/dev/python_workspace/img/gunship1.png')
enm3 = pygame.image.load('e:/dev/python_workspace/img/gunship2.png')
enm4 = pygame.image.load('e:/dev/python_workspace/img/gunship3.png')

# 적우주선 이미지 좌표 변수
enmx = 300
enmy = 0

# 적우주선 다량 출현
enmList = []

# 충돌 체크 함수
def collision():
    global enmy     # 전역 변수화
    for m in mxy:       # 미사일 좌표 리스트에 뽑은 튜플
        dis = pythagoras(enmx-27,enmy-30,m.x,m.y)     # 적우주선과 
        if dis < 30:        # 거리가 30미만이면 -> 적우주선에 미사일에 맞으면
            print('아야')       
            print(dis)
            enmy -= 15       # 적우주선 y좌표가 잠깐 물러남
            m.x = -100      # 미사일을 화면 밖으로 보냄

def makeEnemy():
    e = EnemyShip(random.randint(1,550),50,100,1)       # 적우주선 클래스의 객체 생성
    enmList.append(e)        # 적우주선 객체를 리스트에 담음

class EnemyShip:         # 적우주선 클래스 생성
    def __init__(self,x,y,hp,type):
        self.x = x
        self.y = y
        self.hp = hp        # 기본 체력은 100 보스는 200
        self.type = type        # type 1은 일반 적, 2는 보스
        
    def __del__(self):
        print('적 제거됨')

# 시계 변수
clock = pygame.time.Clock()

cnt = 0
isRunning = True
# 여기 사이의 코드가 반복
while isRunning:
    for event in pygame.event.get():        # 현재 파이게임의 이벤트를 모두 가져와서 하나 씩 꺼냄
        if event.type == pygame.QUIT:       # 창의 x버튼을 누르면 창이 꺼짐
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:        # 마우스 버튼을 누를 때
            # print('마우스 클릭 됨')
            mx, my = pygame.mouse.get_pos()     # 마우스의 위치 좌표를 mx, my에 각각 담암
            mxy.append(Missile(mx,my))      # 미사일 리스트에 Missile 클래스 
            # print(mxy)

    # 배경 그리기
    bgy += 2        # 배경 이미지가 아래로 2씩 이동
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

    # 우주선 플레이어 그리기
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
        if m.y < -19:       # 미사일이 화면 밖으로 사라지면 
            mxy.remove(m)     # 리스트 상에서 지움
            del(m)      # 아예 메모리 상에서 사라짐

    # 적우주선 그리기
    for e in enmList:
        if cnt % 4 == 0:
            screen.blit(enm,(e.x-27,e.y-30))
        elif cnt % 4 == 1:
            screen.blit(enm2,(e.x-27,e.y-30))
        elif cnt % 4 == 2:
            screen.blit(enm3,(e.x-27,e.y-30))
        elif cnt % 4 == 3:
            screen.blit(enm4,(e.x-27,e.y-30))
        e.y += 5

    # 적우주선 객체 생성    
    if cnt % 10 == 0:       # 1/10 비율로 적우주선 객체 생성
        makeEnemy()

    collision()     # 미사일과 적우주선 충돌 발생 여부 체크하는 함수 호출

    pygame.display.update()

pygame.quit()
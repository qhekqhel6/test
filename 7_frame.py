import pygame
import os
###################################################################
# 기본 초기화 (반드시 해야 하느 것들)
pygame.init() # 초기화 반드시 필요

# 화면 크시 설정
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MP3 Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 캐릭터, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/user/Desktop/pygame_basic/pyimg/background.png")

# 캐릭터 불러 오기
unit = pygame.image.load("C:/Users/user/Desktop/pygame_basic/pyimg/unit.png")
unit_size = unit.get_rect().size #이미지의 크기를 구해옴
unit_width = unit_size[0]
unit_height = unit_size[1]
unit_x_pos = screen_width / 2 - unit_width / 2
unit_y_pos = screen_height - unit_height - 30

# 적 캐릭터
unit_1 = pygame.image.load("C:/Users/user/Desktop/pygame_basic/pyimg/unit_1.png")
unit_1_size = unit_1.get_rect().size #이미지의 크기를 구해옴
unit_1_width = unit_1_size[0]
unit_1_height = unit_1_size[1]
unit_1_x_pos = screen_width / 2 - unit_1_width / 2
unit_1_y_pos = screen_height / 2 - unit_1_height - 30

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 60

# 시간 계산
start_ticks = pygame.time.get_ticks() # 시간 tick을 받아옴

# 이동할 좌표
xpos = 0
ypos = 0
# 이동 속도
unit_speed = 3

# 이벤트 루프(이벤트 처리)
running = True # 게임이 실행중인가?
while running:
    dt = clock.tick(60) #프레임

    #print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xpos -= unit_speed
            elif event.key == pygame.K_RIGHT:
                xpos += unit_speed
            elif event.key == pygame.K_UP:
                ypos -= unit_speed
            elif event.key == pygame.K_DOWN:
                ypos += unit_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xpos = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypos = 0

    # 3. 위치 처리             
    unit_x_pos += xpos
    unit_y_pos += ypos

    # 경계값 처리
    if unit_x_pos < 0:
        unit_x_pos = 0
    elif unit_x_pos > screen_width - unit_width:
        unit_x_pos = screen_width - unit_width

    if unit_y_pos < 0:
        unit_y_pos = 0
    elif unit_y_pos > screen_height - unit_height:
        unit_y_pos = screen_height - unit_height

    # 4. 충돌 처리
    unit_rect = unit.get_rect()
    unit_rect.left = unit_x_pos
    unit_rect.top = unit_y_pos

    unit_1_rect = unit_1.get_rect()
    unit_1_rect.left = unit_1_x_pos
    unit_1_rect.top = unit_1_y_pos

    # 5. 충돌 체크
    if unit_rect.colliderect(unit_1_rect):
        print("충돌")
        running = False


    #screen.fill((0, 0, 250))
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(unit, (unit_x_pos, unit_y_pos)) # 캐릭터 그리기
    screen.blit(unit_1, (unit_1_x_pos, unit_1_y_pos)) # 캐릭터 그리기

    # 타이머 넣기
    # 경과 시간 계산 (경과 시간을 1000으로 나누어서 초 (s) 단위로 표기)
    # 출력할 글자, True, 글자 색상
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    
    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("time out")
        running = False

    pygame.display.update()

# 잠시 대기 2초
pygame.time.delay(2000)

# Pygame 종료
pygame.quit()
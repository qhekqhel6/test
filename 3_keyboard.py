import pygame
import os

pygame.init() # 초기화 반드시 필요

# 화면 크시 설정
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MP3 Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/user/Desktop/pygame_basic/pyimg/background.png")

# 캐릭터 불러 오기
unit = pygame.image.load("C:/Users/user/Desktop/pygame_basic/pyimg/unit_1.png")
unit_size = unit.get_rect().size #이미지의 크기를 구해옴
unit_width = unit_size[0]
unit_height = unit_size[1]

unit_x_pos = screen_width / 2 - unit_width / 2
unit_y_pos = screen_height - unit_height - 30


# 이동할 좌표
xpos = 0
ypos = 0

# 이벤트 루프
running = True # 게임이 실행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xpos -= 3
            elif event.key == pygame.K_RIGHT:
                xpos += 3
            elif event.key == pygame.K_UP:
                ypos -= 3
            elif event.key == pygame.K_DOWN:
                ypos += 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xpos = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypos = 0

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


    #screen.fill((0, 0, 250))
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(unit, (unit_x_pos, unit_y_pos)) # 캐릭터 그리기

    pygame.display.update()

# Pygame 종료
pygame.quit()
import pygame
import os
###################################################################
# 기본 초기화 (반드시 해야 하느 것들)
pygame.init() # 초기화 반드시 필요

# 화면 크시 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("probe control demo") # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 캐릭터, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/NEXTRON/Desktop/project/probe_project/background.PNG")

# 캐릭터 불러 오기
probe_1 = pygame.image.load("C:/Users/NEXTRON/Desktop/project/probe_project/probe_1.PNG")
probe_1_size = probe_1.get_rect().size #이미지의 크기를 구해옴
probe_1_width = probe_1_size[0]
probe_1_height = probe_1_size[1]
probe_1_x_pos = 0
probe_1_y_pos = 0

probe_2 = pygame.image.load("C:/Users/NEXTRON/Desktop/project/probe_project/probe_2.PNG")
probe_2_size = probe_2.get_rect().size #이미지의 크기를 구해옴
probe_2_width = probe_2_size[0]
probe_2_height = probe_2_size[1]
probe_2_x_pos = 1280 - probe_2_width
probe_2_y_pos = 0

probe_3 = pygame.image.load("C:/Users/NEXTRON/Desktop/project/probe_project/probe_3.PNG")
probe_3_size = probe_3.get_rect().size #이미지의 크기를 구해옴
probe_3_width = probe_3_size[0]
probe_3_height = probe_3_size[1]
probe_3_x_pos = 0
probe_3_y_pos = 720 - probe_3_height

probe_4 = pygame.image.load("C:/Users/NEXTRON/Desktop/project/probe_project/probe_4.PNG")
probe_4_size = probe_4.get_rect().size #이미지의 크기를 구해옴
probe_4_width = probe_4_size[0]
probe_4_height = probe_4_size[1]
probe_4_x_pos = 1280 - probe_4_width
probe_4_y_pos = 720 - probe_4_height

# center
center = pygame.image.load("C:/Users/NEXTRON/Desktop/project/probe_project/center.png")
center_size = center.get_rect().size #이미지의 크기를 구해옴
center_width = center_size[0]
center_height = center_size[1]
center_x_pos = screen_width / 2 - center_width / 2
center_y_pos = screen_height / 2 - center_height / 2 

#for i in range():
    #unit_1 = unit_1.get_rect(left=random.randint(0, screen_width), unit_1_y_pos = screen_height)
    #units.append(unit_1)

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
# total_time = 60

# 시간 계산
start_ticks = pygame.time.get_ticks() # 시간 tick을 받아옴

# 이동할 좌표
xpos = 0
ypos = 0
# 이동 속도
probe_speed = 1

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
                xpos -= probe_speed
            elif event.key == pygame.K_RIGHT:
                xpos += probe_speed
            elif event.key == pygame.K_UP:
                ypos -= probe_speed
            elif event.key == pygame.K_DOWN:
                ypos += probe_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xpos = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypos = 0
        
        

    # 3. 위치 처리             
    probe_1_x_pos += xpos
    probe_1_y_pos += ypos
    
    # 경계값 처리
    if probe_1_x_pos < 0:
       probe_1_x_pos = 0
    elif probe_1_x_pos > screen_width / 2 - probe_1_width:
        probe_1_x_pos = screen_width / 2 - probe_1_width

    if probe_1_y_pos < 0:
        probe_1_y_pos = 0
    elif probe_1_y_pos > screen_height / 2 - probe_1_height:
        probe_1_y_pos = screen_height / 2 - probe_1_height
   
    

    # 4. 충돌 처리
    probe_1_rect = probe_1.get_rect()
    probe_1_rect.left = probe_1_x_pos
    probe_1_rect.top = probe_1_y_pos

    center_rect = center.get_rect()
    center_rect.left = center_x_pos
    center_rect.top = center_y_pos

        # 5. 충돌 체크
    if probe_1_rect.colliderect(center_rect):
        print("contect")
        #running = False

    
    #screen.fill((0, 0, 250))
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(probe_1, (probe_1_x_pos, probe_1_y_pos)) # 캐릭터 그리기
    screen.blit(probe_2, (probe_2_x_pos, probe_2_y_pos)) # 캐릭터 그리기
    screen.blit(probe_3, (probe_3_x_pos, probe_3_y_pos)) # 캐릭터 그리기
    screen.blit(probe_4, (probe_4_x_pos, probe_4_y_pos)) # 캐릭터 그리기
    screen.blit(center, (center_x_pos, center_y_pos)) # 캐릭터 그리기
    
    #for unit_1 in units:
        #screen.blit(unit_1, units) # 캐릭터 그리기

    # 타이머 넣기
    # 경과 시간 계산 (경과 시간을 1000으로 나누어서 초 (s) 단위로 표기)
    # 출력할 글자, True, 글자 색상
    # elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # screen.blit(timer, (10, 10))
    
    # 만약 시간이 0 이하이면 게임 종료
    #if total_time - elapsed_time <= 0:
    #    print("time out")
    #    running = False

    pygame.display.update()

# 잠시 대기 1초
pygame.time.delay(1000)

# Pygame 종료
pygame.quit()
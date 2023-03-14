import pygame
import os

# 화면 크시 설정
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.init() # 초기화 반드시 필요
# assets 경로 설정
current_path = os.path.dirname(__file__)
img_path = os.path.join(current_path, 'img')

# 배경 이미지 로드
#background_image = pygame.image.load(os.path.join(img_path, 'wheat.jpg'))

# 이미지 로드
#image_1 = pygame.image.load(os.path.join(assets_path), 'mushroom.png')

GRAY = (200, 200, 200) # 색 정의

# 화면 타이틀 설정
pygame.display.set_caption("MP3 Game") # 게임 이름

# 키보드 이미지 로드
keyboard_image = pygame.image.load(os.path.join(img_path, "keyboard.png"))

keyboard_x = int(screen_width / 2)
keyboard_y = int(screen_height / 2)
keyboard_dx = 0
keyboard_dy = 0

# 스크린 정의
#screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock() #게임 화면의 프레임 속도 등을 관리

# 이벤트 루프
done = False # 종료 전까지 반복

while not done:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            done = True # 게임이 진행중
        # 키가 눌린 경우
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -3
            elif event.key == pygame.K_RIGHT:
                keyboard_dx == 3
            elif event.key == pygame.K_UP:
                keyboard_dy == -3
            elif event.key == pygame.K_DOWN:
                keyboard_dy == 3
        # 키가 놓일 경우
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0

    
   
          
# 게임 로직 구간
    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy

# 스크린 채우기
    screen.fill(GRAY)

# 키보드 이미지 그리기
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])

# 버섯 이미지 그리기
# screen.blit(image_1, [100, 100])

# 폰트 선택
#font = pygame.font.SysFont('FixedSys', 40, True, False)

# 글자 표현(텍스트, 안티앨리스 여부, 색상, 배경색)
#text = font.render("Hello MP3", True, BLACK)

# 화면에 텍스트 표시
#screen.blit(text, [200, 600])

# 화면 업데이트 
    pygame.display.flip()

# 초당 60프레임
    clock.tick(60)

# Pygame 종료
pygame.quit() 
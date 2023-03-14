import pygame

# 화면 크시 설정
screen_width = 800
screen_height = 600


BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init() # 초기화 반드시 필요

#화면 타이틀 설정
pygame.display.set_caption("MP3 Game") # 게임 이름

#스크린 정의
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock() #게임 화면의 프레임 속도 등을 관리

# 공 초기 위치, 크기, 속도

ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)
ball_dx = 4
ball_dy = 4
ball_size = 40

# 이벤트 루프
done = False # 종료 전까지 반복

while not done:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            done = True # 게임이 진행중

# 게임 로직 구간
ball_x += ball_dx
ball_y += ball_dy

# 공이 스크린을 벗어나는 경우

if (ball_x + ball_size) > SCREEEN_WIDTH or (ball_x + ball_size) < 0:
    ball_dx = ball_dx * -1
if (ball_y + ball_size) > SCREEEN_HEIGHT or (ball_y + ball_size) < 0:
    ball_dy = ball_dy * -1 
 
# 스크린 채우기

screen.fill(WHITE)

# 공 그리기
pygame.draw.circle(screen, GREEN, [ball_x, ball_y], ball_size, 0)

# 선 그리기
#pygame.draw.line(screen, RED, [50, 50], [500, 50], 10)
#pygame.draw.line(screen, GREEN, [50, 100], [500, 100], 10)
#pygame.draw.line(screen, BLUE, [50, 150], [500, 150], 10)

# 사각형 그리기
# pygame.draw.rect(screen, RED, [50, 200, 150, 150], 4)

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
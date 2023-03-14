import pygame

pygame.init()

# 게임 윈도우 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 캐릭터 이미지 로드
character_img = pygame.image.load("probe_project\probe_1.PNG")
character_rect = character_img.get_rect()

# 캐릭터 초기 위치 설정
character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT // 2
character_rect.center = (character_x, character_y)

# 이동 속도 설정
MOVE_SPEED = 5

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and event.pos == character_rect.center:
            if event.clicks == 2:
                # 더블클릭 이벤트 처리
                character_x, character_y = pygame.mouse.get_pos()
                character_rect.center = (character_x, character_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_x -= MOVE_SPEED
            elif event.key == pygame.K_RIGHT:
                character_x += MOVE_SPEED
            elif event.key == pygame.K_UP:
                character_y -= MOVE_SPEED
            elif event.key == pygame.K_DOWN:
                character_y += MOVE_SPEED

    # 캐릭터 이동 처리
    character_rect.center = (character_x, character_y)

    # 게임 화면 업데이트
    screen.fill((255, 255, 255))
    screen.blit(character_img, character_rect)
    pygame.display.flip()

pygame.quit()

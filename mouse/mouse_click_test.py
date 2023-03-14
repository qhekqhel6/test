import pygame

pygame.init()

clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Title")

character_image = pygame.image.load("probe_project\probe_1.PNG")
character_width = character_image.get_width()
character_height = character_image.get_height()

x = 0
y = 0
double_clicked = False
while not double_clicked:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if event.pos[0] > x and event.pos[0] < x + character_width \
                and event.pos[1] > y and event.pos[1] < y + character_height:
                if event.double:
                    double_clicked = True
    screen.blit(character_image, (x, y))
    pygame.display.update()

    clock.tick(60)

# 잠시 대기 1초
pygame.time.delay(1000)

# Pygame 종료
pygame.quit()

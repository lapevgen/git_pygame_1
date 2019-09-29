import pygame


def draw_flag():
    # рисуем флагшток
    color = pygame.Color(255, 255, 20)
    pygame.draw.rect(screen, color, (20, 20, 30, 420), 0)

    # белая полоса
    color1 = pygame.Color(255, 255, 255)
    pygame.draw.rect(screen, color1, (50, 20, 300, 50), 0)


pygame.init()
size = width, height = 800, 450  # размер окна
screen = pygame.display.set_mode(size)

draw_flag()

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
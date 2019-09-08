import pygame

pygame.init()

size = width, height = 700, 500
screen = pygame.display.set_mode(size)


def flag():
    rect_color = pygame.Color('gray')
    rect_width = 0
    rect_point = [(10, 50), (20, 400)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


flag()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()

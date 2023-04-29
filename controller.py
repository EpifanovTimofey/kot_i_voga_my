import pygame
def p():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
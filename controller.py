import random

import pygame, model

pygame.key.set_repeat(33)
a = pygame.event.custom_type()
pygame.time.set_timer(a, 3000)


def p():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
        if f.type == pygame.KEYDOWN and f.key == pygame.K_RIGHT:
            model.move_r()
        if f.type == pygame.KEYDOWN and f.key == pygame.K_LEFT:
            model.move_l()
        if f.type == a:
            model.o = random.randint(0, 1)

    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])

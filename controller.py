import random

import pygame, model

pygame.key.set_repeat(33)
a = pygame.event.custom_type()
pygame.time.set_timer(a, 3000)
b = pygame.event.custom_type()
pygame.time.set_timer(b, 3000, 1)

def p():
    global  b
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
        if f.type == b:
            pygame.time.set_timer(b, model.speed_zader_kap, 1)
            model.tp_kaplya()
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])

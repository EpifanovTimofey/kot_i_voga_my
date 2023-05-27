import random

import pygame, model

pygame.key.set_repeat(33)
a = pygame.event.custom_type()
pygame.time.set_timer(a, 3000)
pygame.time.set_timer(model.b, 3000, 1)
c = None


def p():
    global b, c
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
        if f.type == model.b:
            pygame.time.set_timer(model.b, model.speed_zader_kap, 1)
            model.tp_kaplya()
        if f.type == model.c:
            model.sun0()
        if f.type == pygame.KEYDOWN and f.key == pygame.K_RETURN:
            model.poyavlenie_sun()
        if f.type == pygame.KEYDOWN and f.key == pygame.K_ESCAPE:
            if model.scena == "play":
                model.game_pause()
                return
    model.show_rects = bool(pygame.key.get_pressed()[pygame.K_TAB])

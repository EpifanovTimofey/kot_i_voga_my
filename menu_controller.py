import pygame

import model
def p():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.KEYDOWN and f.key == pygame.K_SPACE:
            model.game()
        if f.type == pygame.MOUSEBUTTONDOWN and f.button == pygame.BUTTON_LEFT and model.rect_knopka.collidepoint(f.pos):
            model.game()
        if f.type == pygame.QUIT:
            exit()
def p2():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.KEYDOWN and f.key == pygame.K_ESCAPE:
            model.game()
        if f.type == pygame.QUIT:
            exit()
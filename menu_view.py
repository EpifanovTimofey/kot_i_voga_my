import pygame

import model

b = pygame.display.set_mode([800, 600])
text_shrift = pygame.font.SysFont("arial", 125)
text_shrift1 = pygame.font.SysFont("arial", 40)

def a():
    d1 = pygame.draw.rect(b, [200, 200, 200], [350, 200, 30, 150])
    d2 = pygame.draw.rect(b, [200, 200, 200], [400, 200, 30, 150])
    d1.center = [370, 300]
    d2.center = [430, 300]
    pygame.display.flip()

def m():
    pygame.draw.rect(b, [20, 200, 20], [0, 0, 800, 600])
    pygame.draw.rect(b, [200, 20, 20], model.rect_knopka)
    text1 = text_shrift.render("ИГРАТЬ", True, [255, 255, 255])
    b.blit(text1, [200, 227])
    text1 = text_shrift1.render("Лучший результат: " + str(model.resultat), True, [0, 0, 0])
    b.blit(text1, [10, 10])
    pygame.display.flip()
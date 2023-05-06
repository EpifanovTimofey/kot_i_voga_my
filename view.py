import pygame, model
from pygame import display, draw, image, transform

dis = display.set_mode([800, 600])
cat = image.load("pics/cat1.png")
zontik = image.load("pics/umbrella.png")
vedro = image.load("pics/bucket.png")
zontik1 = transform.scale(zontik, model.rect_zontik.size)
vedro1 = transform.scale(vedro, model.rect_vedro.size)
cat1 = pygame.transform.flip(cat, True, False)
zontik2 = pygame.transform.flip(zontik1, True, False)
vedro2 = pygame.transform.flip(vedro1, True, False)

def flip():
    dis.fill([0, 0, 0])
    if model.show_rects:
        draw.rect(dis, [10, 200, 30], model.rect_cat, 3)
        draw.rect(dis, [30, 200, 200], model.rect_zontik, 3)
        draw.rect(dis, [100, 100, 255], model.rect_vedro, 3)
    if model.reverse == True:
        dis.blit(cat1, model.rect_cat)
        dis.blit(zontik2, model.rect_zontik)
        dis.blit(vedro2, model.rect_vedro)
    if model.reverse == False:
        dis.blit(cat, model.rect_cat)
        dis.blit(zontik1, model.rect_zontik)
        dis.blit(vedro1, model.rect_vedro)
    display.flip()
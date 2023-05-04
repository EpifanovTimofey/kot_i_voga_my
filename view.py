import pygame, model
from pygame import display, draw, image, transform

dis = display.set_mode([800, 600])
cat = image.load("pics/cat1.png")
zontik1 = image.load("pics/umbrella.png")
vedro1 = image.load("pics/bucket.png")
def flip():
    dis.fill([0,0,0])
    zontik = transform.scale(zontik1, model.rect_zontik.size)
    vedro = transform.scale(vedro1, model.rect_vedro.size)
    draw.rect(dis, [10, 200, 30], model.rect_cat, 3)
    draw.rect(dis, [30, 200, 200], model.rect_zontik, 3)
    draw.rect(dis, [100, 100, 255], model.rect_vedro, 3)
    dis.blit(cat, model.rect_cat)
    dis.blit(zontik, model.rect_zontik)
    dis.blit(vedro, model.rect_vedro)
    display.flip()

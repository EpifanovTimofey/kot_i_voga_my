import pygame, model
from pygame import display, draw, image, transform

dis = display.set_mode([800, 600])
cat = image.load("pics/cat1.png")
zontik = image.load("pics/umbrella.png")
vedro = image.load("pics/bucket.png")
oblako = image.load("pics/cloud.png")
kaplya = image.load("pics/water_drop.png")
voda = image.load("pics/water.png")
plot = image.load("pics/raft.png")
zontik1 = transform.scale(zontik, model.rect_zontik.size)
vedro1 = transform.scale(vedro, model.rect_vedro.size)
oblako1 = transform.scale(oblako, model.rect_oblako.size)
kaplya1 = transform.scale(kaplya, model.rect_kaplya.size)
voda1 = transform.scale(voda, model.rect_voda.size)
plot1 = transform.scale(plot, model.rect_plot.size)
cat1 = pygame.transform.flip(cat, True, False)
zontik2 = pygame.transform.flip(zontik1, True, False)
vedro2 = pygame.transform.flip(vedro1, True, False)


def flip():
    dis.fill([0, 0, 0])
    dis.blit(kaplya1, model.rect_kaplya)
    dis.blit(oblako1, model.rect_oblako)
    dis.blit(voda1, model.rect_voda)
    draw.rect(dis, [49, 145, 192], [0, model.rect_voda.bottom, 800, 600-model.rect_voda.bottom])
    dis.blit(plot1, model.rect_plot)
    if model.reverse == True:
        dis.blit(cat1, model.rect_cat)
        dis.blit(zontik2, model.rect_zontik)
        dis.blit(vedro2, model.rect_vedro)
    if model.reverse == False:
        dis.blit(cat, model.rect_cat)
        dis.blit(zontik1, model.rect_zontik)
        dis.blit(vedro1, model.rect_vedro)
    if model.show_rects:
        draw.rect(dis, [10, 200, 30], model.rect_cat, 3)
        draw.rect(dis, [30, 200, 200], model.rect_zontik, 3)
        draw.rect(dis, [100, 100, 255], model.rect_vedro, 3)
        draw.rect(dis, [200, 200, 200], model.rect_oblako, 3)
        draw.rect(dis, [0, 200, 255], model.rect_kaplya, 3)
        draw.rect(dis, [200, 150, 100], model.rect_voda, 3)
        draw.rect(dis, [245, 255, 36], model.rect_plot, 3)
    display.flip()

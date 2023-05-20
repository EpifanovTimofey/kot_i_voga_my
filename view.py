import pygame, model
from pygame import display, draw, image, transform

pygame.init()
dis = display.set_mode([800, 600])
cat = image.load("pics/cat1.png")
zontik = image.load("pics/umbrella.png")
vedro = image.load("pics/bucket.png")
oblako = image.load("pics/cloud.png")
kaplya = image.load("pics/water_drop.png")
voda = image.load("pics/water.png")
plot = image.load("pics/raft.png")
sun = image.load("pics/sun.png")
zontik1 = transform.scale(zontik, model.rect_zontik.size)
vedro1 = transform.scale(vedro, model.rect_vedro.size)
oblako1 = transform.scale(oblako, model.rect_oblako.size)
kaplya1 = transform.scale(kaplya, model.rect_kaplya.size)
voda1 = transform.scale(voda, model.rect_voda.size)
sun1 = transform.scale(sun, model.rect_sun.size)
plot1 = transform.scale(plot, model.rect_plot.size)
cat1 = pygame.transform.flip(cat, True, False)
zontik2 = pygame.transform.flip(zontik1, True, False)
vedro2 = pygame.transform.flip(vedro1, True, False)
sun1 = pygame.transform.flip(sun1, True, False)
text_shrift = pygame.font.SysFont("arial", 40)


def flip():
    dis.fill([0, 0, 0])
    dis.blit(sun1, model.rect_sun)
    dis.blit(kaplya1, model.rect_kaplya)
    dis.blit(oblako1, model.rect_oblako)
    dis.blit(voda1, model.rect_voda)
    draw.rect(dis, [49, 145, 192], [0, model.rect_voda.bottom, 800, 600 - model.rect_voda.bottom])
    dis.blit(plot1, model.rect_plot)
    text1 = text_shrift.render(str(model.kapli1) + " кап" + kapli_text(model.kapli1), True, [153, 148, 255])
    dis.blit(text1, [10, 10])
    text2 = text_shrift.render(str(model.vsego_kapel) + " кап" + kapli_text(model.vsego_kapel) + " до ускорения", True,
                               [153, 148, 255])
    dis.blit(text2, [10, 50])
    text3 = text_shrift.render(str(model.urov) + " уровень", True, [153, 148, 255])
    dis.blit(text3, [10, 90])
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


def kapli_text(abc):
    if abc == 0 or (abc >= 5 and abc <= 20) or (
            abc % 10 >= 5 and abc % 10 <= 9) or abc % 10 == 0:
        ok = "ель"
    elif abc % 10 == 1:
        ok = "ля"
    elif abc % 10 >= 2 and abc % 10 <= 4:
        ok = "ли"
    return ok

import random

import pygame

rect_voda = pygame.Rect([0, 560, 800, 30])
rect_plot = pygame.Rect([100, rect_voda.top, 210, 50])
rect_cat = pygame.Rect([100, rect_plot.top - 100, 167, 126])
rect_zontik = pygame.Rect([rect_cat.left + 95, rect_cat.top - 80, 70, 100])
rect_vedro = pygame.Rect([rect_cat.left - 17, rect_cat.top - 35, 70, 70])
rect_oblako = pygame.Rect([random.randint(0, 700), 35, 100, 70])
rect_kaplya = pygame.Rect([rect_oblako.left + 35, 55, 15, 20])
rect_sun = pygame.Rect([670, 10, 120, 120])
show_rects = False
reverse = False
o = 1
kapli1 = 0
vsego_kapel = 5
speed_ob = 3
speed_kap = 3
urov = 1
speed_zader_kap = 3000


def move_r():
    global reverse
    if rect_vedro.right < 800:
        rect_vedro.left += 10
        reverse = True
        povorot_r1()


def move_l():
    global reverse
    if rect_vedro.left > 0:
        rect_vedro.left -= 10
        move_l1()
        reverse = False


def move_ob():
    global o
    if o == 1 and rect_oblako.left >= 0:
        rect_oblako.left -= speed_ob
    else:
        o = 0
    if o == 0 and rect_oblako.right <= 800:
        rect_oblako.right += speed_ob
    else:
        o = 1


def move_l1():
    rect_cat.left = rect_vedro.left + 17
    rect_zontik.left = rect_cat.left + 95
    rect_plot.left = rect_cat.left


def povorot_r1():
    rect_cat.right = rect_vedro.right - 17
    rect_zontik.right = rect_cat.right - 95
    rect_plot.right = rect_cat.right

def move_kaplya():
    global rect_kaplya, kapli1
    rect_kaplya.top += speed_kap
    if rect_kaplya.colliderect(rect_zontik):
        rect_kaplya.left = 900
    if rect_kaplya.colliderect(rect_vedro):
        rect_kaplya.left = 900
        kapli1 += 1
    if rect_kaplya.colliderect(rect_voda):
        move_voda()
        rect_kaplya.left = 900


def tp_kaplya():
    global vsego_kapel, speed_ob, speed_kap, urov, speed_zader_kap
    if rect_kaplya.bottom < rect_voda.top:
        return
    rect_kaplya.centerx = rect_oblako.centerx
    rect_kaplya.top = rect_oblako.top
    vsego_kapel -= 1
    if vsego_kapel == 0:
        vsego_kapel = 5
        if speed_ob < 8:
            speed_ob += 1
        if speed_kap < 9:
            speed_kap += 1
        urov += 1
        if urov >= 4:
            speed_zader_kap -= 250
        if speed_zader_kap <= 500:
            speed_zader_kap = 500



def move_voda():
    rect_voda.top -= 8
    rect_plot.top = rect_voda.top
    rect_cat.top = rect_plot.top - 100
    rect_zontik.top = rect_cat.top - 80
    rect_vedro.top = rect_cat.top - 35
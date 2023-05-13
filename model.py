import random

import pygame

rect_voda = pygame.Rect([0, 470, 800, 30])
rect_plot = pygame.Rect([100, rect_voda.top, 210, 50])
rect_cat = pygame.Rect([100, rect_plot.top - 100, 167, 126])
rect_zontik = pygame.Rect([rect_cat.left + 95, rect_cat.top - 80, 70, 100])
rect_vedro = pygame.Rect([rect_cat.left - 17, rect_cat.top - 35, 70, 70])
rect_oblako = pygame.Rect([random.randint(0, 700), 35, 100, 70])
rect_kaplya = pygame.Rect([rect_oblako.left + 25, 55, 25, 40])
show_rects = False
reverse = False
o = 1

#470
def move_r():
    global reverse
    if rect_vedro.right < 800:
        rect_vedro.left += 8
        reverse = True
        povorot_r1()


def move_l():
    global reverse
    if rect_vedro.left > 0:
        rect_vedro.left -= 8
        move_l1()
        reverse = False


def move_ob():
    global o
    if o == 1 and rect_oblako.left >= 0:
        rect_oblako.left -= 3
    else:
        o = 0
    if o == 0 and rect_oblako.right <= 800:
        rect_oblako.right += 3
    else:
        o = 1


def move_l1():
    rect_cat.left = rect_vedro.left + 17
    rect_zontik.left = rect_cat.left + 95


def povorot_r1():
    rect_cat.right = rect_vedro.right - 17
    rect_zontik.right = rect_cat.right - 95


def move_kaplya():
    rect_kaplya.top += 3


def tp_kaplya():
    rect_kaplya.centerx = rect_oblako.centerx
    rect_kaplya.top = rect_oblako.top


def move_voda():
    rect_voda.top = random.randint(0, 570)
    rect_plot.top = rect_voda.top

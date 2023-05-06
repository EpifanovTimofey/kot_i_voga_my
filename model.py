import pygame

rect_cat = pygame.Rect([100, 470, 167, 126])
rect_zontik = pygame.Rect([rect_cat.left + 95, 390, 70, 100])
rect_vedro = pygame.Rect([rect_cat.left - 17, 435, 70, 70])
show_rects = False
reverse = False

def move_r():
    global reverse
    rect_cat.left += 4
    move_lr()
    reverse = True
    povorot()

def move_l():
    global reverse
    if rect_vedro.left > 0:
        rect_cat.left -= 4
        move_lr()
        reverse = False

def move_lr():
    rect_zontik.left = rect_cat.left + 95
    rect_vedro.left = rect_cat.left - 17

def povorot():
    rect_zontik.right = rect_cat.right - 95
    rect_vedro.right = rect_cat.right + 17
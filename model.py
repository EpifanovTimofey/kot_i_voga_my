import pygame,random
rect_cat = pygame.Rect([100,470,167,126])
rect_zontik = pygame.Rect([rect_cat.left+95,390,70,100])
rect_vedro = pygame.Rect([rect_cat.left-17,435,70,70])
def move():
    rect_cat.left = random.randint(50,450)
    rect_zontik.left = rect_cat.left+95
    rect_vedro.left = rect_cat.left-17
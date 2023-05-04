import pygame,model
def p():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
        if f.type == pygame.KEYDOWN:
            if f.key == pygame.K_SPACE:
                model.move()
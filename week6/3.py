import pygame 
from random import randrange
pygame.init()
size = (800,800)
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
color = (255,0,0)
clock = pygame.time.Clock()
done = False 
block = 50
x = randrange(0,800, block)
y = randrange(0,800, block)
while not done: 
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 20    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 20
    if x > 800:
        x = 0
    if x < 0:
        x = 800
    if y > 800:
        y = 0
    if y < 0:
        y = 800
    pygame.draw.circle(screen, color,(x,y) ,25)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()

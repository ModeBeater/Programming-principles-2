import pygame 
import random


ok = True
menu = True
running = True
while ok:
    money = 0
    pygame.init()
    pygame.display.set_caption("Racer")
    road = pygame.image.load('road.png')
    enemy = pygame.image.load('enemy.png')
    car = pygame.image.load('car.png')
    coin = pygame.image.load('coin.png')
    ecoin = pygame.image.load('ecoin.png')
    size = road.get_size()
    size1 = car.get_size()
    size2 = enemy.get_size()
    size3 = coin.get_size()
    size4 = ecoin.get_size()
    font_end = pygame.font.SysFont('Arial', 66, bold = True)
    font_money = pygame.font.SysFont('Arial', 30, bold = True)
    screen = pygame.display.set_mode(size)
    FPS = 60
    x = random.randint(180,620)
    y = 540
    x1 = random.randint(180,620)
    y1 = 0
    Clock = pygame.time.Clock()
    dy = 5
    cnt = 0
    x2 = random.randint(180,620)
    y2 = random.randint(0,400)
    x3 = random.randint(180,620)
    y3 = random.randint(0,400)
    bol = 0
    while running:
        pygame.display.flip()
        Clock.tick(FPS)
        menu = True
        screen.blit(road, (0,0))
        screen.blit(enemy,(x1,y1))
        if bol == 0:
            screen.blit(coin,(x2,y2))
        if bol == 1:
            screen.blit(ecoin,(x2,y2))
        y2 += 5
        screen.blit(car,(x,y))
        render_money = font_money.render(f'Coins: {money}', True, pygame.Color('Black'))
        screen.blit(render_money, (680,0))
        pressed = pygame.key.get_pressed()
        y1 += dy
        if y2 > size[1]:
            y2 = 0
        if y1 > size[1]:
            x1 = random.randint(180,620)
            y1 = 0
            cnt += 1
            if money % 5 == 0:
                dy += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                menu = False
                ok = False
                pygame.quit()
        if pressed[pygame.K_UP] and y > 0:
            y -= 10
        if pressed[pygame.K_DOWN] and y < 550:
            y += 10
        if pressed[pygame.K_LEFT] and x > 180:
            x -= 10   
        if pressed[pygame.K_RIGHT] and x < 620:
            x += 10
        if bol == 1:
            if y <= y2 + size4[1] and y >= y2 - size1[1] and x <= x2 + size1[0] and x >= x2 - size4[0]:
                c = random.randint(1,10)
                if money > 10:
                    y3 = random.randint(0,400)
                    x3 = random.randint(180,620)
                    while y <= y2 + size4[1] and y >= y2 - size1[1] and x <= x2 + size1[0] and x >= x2 - size4[0]:
                        y2 = random.randint(0,400)
                        x2 = random.randint(180,620)
                    if c % 2 == 0:
                        bol = 0
                    if c % 2 == 1:
                        bol = 1
                    money += 2
        if bol == 0:
            if y <= y2 + size3[1] and y >= y2 - size1[1] and x <= x2 + size1[0] and x >= x2 - size3[0]:
                c = random.randint(1,10)
                if money > 10:
                    y2 = random.randint(0,400)
                    x2 = random.randint(180,620)
                    while y <= y2 + size3[1] and y >= y2 - size1[1] and x <= x2 + size1[0] and x >= x2 - size3[0]:
                        y2 = random.randint(0,400)
                        x2 = random.randint(180,620)
                    if c % 2 == 0:
                        bol = 0
                    if c % 2 == 1:
                        bol = 1
                if money <= 10:
                    y2 = random.randint(0,400)
                    x2 = random.randint(180,620)
                    while y <= y2 + size3[1] and y >= y2 - size1[1] and x <= x2 + size1[0] and x >= x2 - size3[0]:
                        y2 = random.randint(0,400)
                        x2 = random.randint(180,620)
                money += 1
       
        if y <= y1 + size1[1] and y >= y1 - size2[1] and x <= x1 + size1[0] and x >= x1 - size2[0]:
            running = False
    while menu:
        pygame.display.flip()
        Clock.tick(FPS)
        screen.blit(road, (0,0))
        render_end = font_end.render('GAME OVER',True, pygame.Color('black'))
        render_end1 = font_end.render('Press Space',True, pygame.Color('black'))
        screen.blit(render_end, (200, 200))
        screen.blit(render_end1, (200,300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                menu = False
                ok = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = True
                menu = False
pygame.quit()
import pygame
import random 
from datetime import timedelta
from datetime import datetime
ok = True
menu = True
running = True

while ok:
    dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
    pygame.init()
    screen = pygame.display.set_mode((960,800))
    pygame.display.set_caption("Snake")
    fon = pygame.image.load('snake.jpg')
    x = random.randrange(20,940,20)
    y = random.randrange(120,780,20)
    x1 = random.randrange(20,940,20)
    y1 = random.randrange(120,780,20)
    x2 = random.randrange(120,780,20)
    y2 = random.randrange(120,780,20)
    speed = 10
    running = True
    snake = [[x,y]]
    length = 1
    FPS = 30
    dx = 0
    dy = 0
    level = 1
    score = 0
    bol = 0
    font_end = pygame.font.SysFont('Arial', 66, bold = True)
    font_score = pygame.font.SysFont('Arial', 30, bold = True)
    font_level = pygame.font.SysFont('Arial', 30, bold = True)
    def move(snake,dx,dy):
        snake[0][0] += dx
        snake[0][1] += dy
    clock = pygame.time.Clock()
    z = int(datetime.now().strftime("%S"))
    # print(z)
    count = 0
    while running:
        d = int(datetime.now().strftime("%S"))
        menu = True
        clock.tick(speed) 
        screen.fill((0,0,0))
        # screen.blit(fon, (10,100))
        render_score = font_score.render(f'Score: {score}', True, pygame.Color('Red'))
        render_level = font_score.render(f'Level:  {level}', True, pygame.Color('Red'))
        screen.blit(render_level, (805, 50))
        screen.blit(render_score, (805,20))
        for i in snake:
            pygame.draw.circle(screen, (0, 255,0), i, 10)
        for i in range(length - 1, 0, -1):
            snake[i][0] = snake[i - 1][0]
            snake[i][1] = snake[i - 1][1]
        pygame.draw.rect(screen, (255, 255, 255), (0,100,960,800), 10)
        pygame.draw.rect(screen, (255, 255, 255), (0,0,960,800), 10)
        # pygame.draw.rect(screen, (255, 255, 255), (480,400,500,400))
        pygame.draw.line(screen, (255, 255, 255), (480,400),(500,400), 100)
        if bol == 0:
            pygame.draw.circle(screen, (255,0,0), (x1,y1), 10)
        if bol == 1:
            pygame.draw.circle(screen, (255,255,0), (x2,y2), 10)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
                ok = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menu = False
                    ok = False
        if key[pygame.K_RIGHT] and dirs['RIGHT']:
            dx = 20
            dy = 0
            dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
        if key[pygame.K_LEFT] and dirs['LEFT']:
            dx = -20
            dy = 0
            dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
        if key[pygame.K_UP] and dirs['UP']:
            dx = 0
            dy = -20
            dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
        if key[pygame.K_DOWN] and dirs['DOWN']:
            dx = 0
            dy = 20
            dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
        if z == d - 10:
            x1 = random.randrange(20,940,20)
            y1 = random.randrange(120,780,20)
            for i in range(length - 1, 0, -1):
                while snake[i][0] == x1 and snake[i][1] == y1:
                    x1 = random.randrange(20,940,20)
                    y1 = random.randrange(120,780,20)
            z = d
        if snake[0][0] == x1 and snake[0][1] == y1:
            c = random.randint(1,10)
            if score > 10:
                x1 = random.randrange(20,940,20)
                y1 = random.randrange(120,780,20)
                for i in range(length - 1, 0, -1):
                    while snake[i][0] == x1 and snake[i][1] == y1:
                        x1 = random.randrange(20,940,20)
                        y1 = random.randrange(120,780,20)
                if c % 2 == 0:
                    bol = 0
                if c % 2 == 1:
                    bol = 1
                score += 1
                length += 1
                snake.append([0,0])
            if score <= 10:
                x1 = random.randrange(20,940,20)
                y1 = random.randrange(120,780,20)
                for i in range(length - 1, 0, -1):
                    while snake[i][0] == x1 and snake[i][1] == y1:
                        x1 = random.randrange(20,940,20)
                        y1 = random.randrange(120,780,20)
                bol = 0
                score += 1
                length += 1
                snake.append([0,0])
            if score % 5 == 0:
                speed += 2
                level += 1
            z = d 
        if snake[0][0] == x2 and snake[0][1] == y2:
            c = random.randint(1,10)
            if score >= 10:
                x2 = random.randrange(20,940,20)
                y2 = random.randrange(120,780,20)
                for i in range(length - 1, 0, -1):
                    while snake[i][0] == x2 and snake[i][1] == y2:
                        x2 = random.randrange(20,940,20)
                        y2 = random.randrange(120,780,20)
                if c % 2 == 0:
                    bol = 0
                if c % 2 == 1:
                    bol = 1
                score += 2
                length += 2
                snake.append([0,0])
                snake.append([0,0])
            z = d
            if score % 5 == 0:
                speed += 2
                level += 1
        # print(snake)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if snake[0][0] < 10 or snake[0][0] > 950 or snake[0][1] < 110 or snake[0][1] > 790:
            running = False
        if (snake[0][0] >= 480 and snake[0][1] <= 450 and snake[0][1] >= 350 and snake[0][0] <= 500):
            running = False
        elif length > 4:
            for i in range(4, len(snake)):
                if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                    running = False
        move(snake,dx,dy)
        pygame.display.update()
    while menu:
        pygame.display.flip()
        clock.tick(FPS)
        screen.fill((0,0,0))
        render_end = font_end.render('GAME OVER',True, pygame.Color('red'))
        render_end1 = font_end.render('PRESS SPACE',True, pygame.Color('red'))
        render_score = font_score.render(f'Score: {score}', True, pygame.Color('Red'))
        render_level = font_score.render(f'Level:  {level}', True, pygame.Color('Red'))
        screen.blit(render_level, (805, 50))
        screen.blit(render_score, (805,20))
        screen.blit(render_end, (280, 300))
        screen.blit(render_end1, (250, 400))
        pygame.draw.rect(screen, (255, 255, 255), (0,100,960,800), 10)
        pygame.draw.rect(screen, (255, 255, 255), (0,0,960,800), 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                ok = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = False
                    ok = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = True
                menu = False
pygame.quit()
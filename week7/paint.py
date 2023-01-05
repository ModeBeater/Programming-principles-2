import pygame

pygame.init()
screen = pygame.display.set_mode((900,800))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
surf = pygame.Surface((900,800))
FPS = 60
draw = False
running = True
lastPos = (0,0)
radius = 5
color = 'black'
mode = 'pen'
pen = pygame.image.load('pen.png')
eraser = pygame.image.load('eraser.png')
def drawing(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if x2 < 100: 
        return 
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1,x2):
            y = (-c - a * x) / b
            pygame.draw.circle(screen,pygame.Color(color), (x,y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1,y2):
            x = (-c - b * y) / a
            pygame.draw.circle(screen,pygame.Color(color), (x,y), width)        
def drawCircle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x,y), radius, width)
def drawRectangle(surf, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(surf,pygame.Color(color), (x1,y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(surf,pygame.Color(color), (x2,y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(surf,pygame.Color(color), (x2,y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(surf,pygame.Color(color), (x1,y2, widthr, height), width)
def drawSquare(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widths = abs(x1 - x2)
    height = abs(y1 - y2)
    if widths <= height:
        size = widths
    if height <= widths:
        size = height
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen,pygame.Color(color), (x1,y1, size, size), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen,pygame.Color(color), (x2,y1, size, size), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen,pygame.Color(color), (x2,y2, size, size), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen,pygame.Color(color), (x1,y2, size, size), width)        
def drawRightTriangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1), (x2,y2), (x1,y2)), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1), (x2,y2), (x1,y2)), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1), (x2,y2), (x2,y1)), width)    
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1), (x2,y2), (x2,y1)), width)  
def drawEquilaterialTriangle(screen,start, end,width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    width_e = abs(x2 - x1)
    height = (3**0.5) * width_e / 2
    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y2), (x2,y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1), (x2,y1), ((x1 + x2) / 2, y1 - height)), width)  
def drawRhombus(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.polygon(screen, pygame.Color(color), (((x1 + x2) / 2, y1), (x2, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x1, (y1 + y2) / 2)), width)       
screen.fill(pygame.Color('white'))
surf.fill(pygame.Color('white'))
e = 0
ok = 0
while running:
    # screen.fill(pygame.Color('white'))
    # screen.blit(surf, (0,0))
    pygame.draw.rect(screen,pygame.Color('white'), (0,0, 100, 800))
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 100), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 180), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 270), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 360), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 540), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 605), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 670), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 735), 10)
    pygame.draw.rect(screen,pygame.Color('black'), (0,0, 100, 800), 10)
    pygame.draw.circle(screen, pygame.Color('red'), (30, 375), 15)
    pygame.draw.circle(screen, pygame.Color('blue'), (65, 375), 15)
    pygame.draw.circle(screen, pygame.Color('black'), (30, 410), 15)
    pygame.draw.circle(screen, pygame.Color('yellow'), (65, 410), 15)
    pygame.draw.circle(screen, pygame.Color('green'), (30, 445), 15)
    pygame.draw.circle(screen, pygame.Color('orange'), (65, 445), 15)
    pygame.draw.circle(screen, pygame.Color('purple'), (30, 480), 15)
    pygame.draw.circle(screen, pygame.Color('pink'), (65, 480), 15)
    pygame.draw.circle(screen, pygame.Color('grey'), (30, 515), 15)
    pygame.draw.circle(screen, pygame.Color('brown'), (65, 515), 15)
    pygame.draw.rect(screen,pygame.Color('black'), (25,545, 45, 45), 5)
    pygame.draw.polygon(screen, pygame.Color('black'), ((25,610), (80,650), (25,650)), 5)
    pygame.draw.polygon(screen, pygame.Color('black'), ((20,720), (75,720), (47, 675)), 5)
    pygame.draw.polygon(screen, pygame.Color('black'), ((50, 740), (75, 765), (50, 790), (25, 765)), 5)
    screen.blit(eraser,(12,272))
    screen.blit(pen,(10,10))
    clock.tick(FPS)
    pygame.draw.rect(screen,pygame.Color('black'), (15,110, 70, 50), 5)
    pygame.draw.circle(screen, pygame.Color('black'), (50, 220), 35, 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            e = 1
            # print(event.pos)
            if event.pos[0] < 90 and event.pos[1] < 90 and event.pos[1] > 10:
                mode = 'pen'
                draw = False
            if event.pos[0] < 90 and event.pos[1] > 100 and event.pos[1] < 170:
                mode = 'rectangle'
                draw = False
            if event.pos[0] >= 15 and event.pos[0] <= 45 and event.pos[1] >= 360 and event.pos[1] <= 390:
                mode = 'pen'
                color = 'red'
                draw = False
            if event.pos[0] >= 50 and event.pos[0] <= 80 and event.pos[1] >= 360 and event.pos[1] <= 390:
                mode = 'pen'
                color = 'blue'
                draw = False
            if event.pos[0] >= 15 and event.pos[0] <= 45 and event.pos[1] >= 395 and event.pos[1] <= 420:
                mode = 'pen'
                color = 'black'
                draw = False
            if event.pos[0] >= 50 and event.pos[0] <= 80 and event.pos[1] >= 395 and event.pos[1] <= 425:
                mode = 'pen'
                color = 'yellow'
                draw = False
            if event.pos[0] >= 15 and event.pos[0] <= 45 and event.pos[1] >= 430 and event.pos[1] <= 460:
                mode = 'pen'
                color = 'green'
                draw = False
            if event.pos[0] >= 50 and event.pos[0] <= 80 and event.pos[1] >= 430 and event.pos[1] <= 460:
                mode = 'pen'
                color = 'orange'
                draw = False
            if event.pos[0] >= 15 and event.pos[0] <= 45 and event.pos[1] >= 465 and event.pos[1] <= 495:
                mode = 'pen'
                color = 'purple'
                draw = False
            if event.pos[0] >= 50 and event.pos[0] <= 80 and event.pos[1] >= 465 and event.pos[1] <= 495:
                mode = 'pen'
                color = 'pink'
                draw = False
            if event.pos[0] >= 15 and event.pos[0] <= 45 and event.pos[1] >= 500 and event.pos[1] <= 530:
                mode = 'pen'
                color = 'grey'
                draw = False
            if event.pos[0] >= 50 and event.pos[0] <= 80 and event.pos[1] >= 500 and event.pos[1] <= 530:
                mode = 'pen'
                color = 'brown'
                draw = False
            if event.pos[0] < 90 and event.pos[1] > 180 and event.pos[1] < 260:
                mode = 'circle'
                draw = False
            if event.pos[0] >= 25 and event.pos[0] <= 70 and event.pos[1] >= 545 and event.pos[1] <= 590:
                mode = 'square'
                draw = False
            if event.pos[0] < 90 and event.pos[1] > 270 and event.pos[1] < 350:
                mode = 'eraser'
                draw = False
            if event.pos[0] >= 25 and event.pos[0] <= 80 and event.pos[1] >= 610 and event.pos[1] <= 650:
                mode = 'rightTriangle'
                draw = False
            if event.pos[0] >= 18 and event.pos[0] <= 80 and event.pos[1] >= 675 and event.pos[1] <= 725:
                mode = 'EquilaterialTrinagle'
                draw = False
            if event.pos[0] >= 25 and event.pos[0] <= 75 and event.pos[1] >= 740 and event.pos[1] <= 790:
                mode = 'Rhombus'
                draw = False
            elif event.pos[0] < 100:
                draw = False
            if event.pos[0] > 100:
                draw = True
                prevPos = event.pos
                if mode == 'pen':
                    pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
                if mode == 'eraser':
                    pygame.draw.circle(screen, pygame.Color('white'), event.pos, radius)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            radius = max(1, radius - 1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            radius = min(200, radius + 1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            screen.fill(pygame.Color('white'))
        if event.type == pygame.MOUSEBUTTONUP:
            e = 0
            ok = 0
            if mode == 'rectangle' and draw == True:
                drawRectangle(surf, prevPos, event.pos, radius, color)
            elif mode == 'circle' and draw == True:
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'square' and draw == True:
                drawSquare(screen, prevPos, event.pos, radius, color)
            elif mode == 'rightTriangle' and draw == True:
                drawRightTriangle(screen,prevPos, event.pos, radius, color)
            elif mode == 'EquilaterialTrinagle' and draw == True:
                drawEquilaterialTriangle(screen,prevPos,event.pos,radius,color)
            elif mode == 'Rhombus' and draw == True:
                drawRhombus(screen,prevPos,event.pos,radius,color)
            draw = False
        if event.type == pygame.MOUSEMOTION and e == 1:
            if mode == 'rectangle' and draw == True:
                drawRectangle(screen, prevPos, event.pos, radius, color)
            if draw == True and mode == 'pen' and event.pos[0] > 100:
                drawing(screen, lastPos, event.pos, radius, color)
            if draw == True and mode == 'eraser' and event.pos[0] > 100:
                drawing(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos
    
    pygame.display.update()
pygame.quit()

import pygame 

song = ['1op.mp3', '2op.mp3', '3op.mp3']
pygame.init()
image1 = pygame.image.load('6.jpg')
image2 = pygame.image.load('10.jpg')
image3 = pygame.image.load('12.jpeg')
image = [image1, image2, image3]
play = pygame.image.load('8.png')
pause = pygame.image.load('10.png')
p1 = pygame.image.load('6.png')
p2 = pygame.image.load('7.png')
size = width, height = image1.get_size()
font_play = pygame.font.SysFont('Arial', 26, bold = True)
screen = pygame.display.set_mode(size)
done = False 
pygame.mixer.music.load('1op.mp3')
cnt = 0
a = 0
count = 0
while not done:
    pygame.display.flip()
    screen.blit(image[cnt],(0,0))
    if a == 0:
        screen.blit(play,(500,500))
        render_play = font_play.render(f'will play: {song[cnt]}', True, pygame.Color('White'))
        screen.blit(render_play, (0, 10))
    if a == 1:
        screen.blit(pause,(500,500))
        render_play = font_play.render(f'Now playing: {song[cnt]}', True, pygame.Color('White'))
        screen.blit(render_play, (0, 10))
    screen.blit(p1,(350,500))
    screen.blit(p2,(670, 480))
    for event in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and 535 <= mx <= 660 and 515 <= my <= 647 and a == 0:
            if count == 0:
                pygame.mixer.music.play(-1)
                count += 1
            pygame.mixer.music.unpause()
            screen.blit(play,(500,500))
            a = 1
            break
        if event.type == pygame.MOUSEBUTTONDOWN and 390 <= mx <= 515 and 515 <= my <= 647:
            cnt -= 1
            if cnt < 0:
                cnt = len(song) - 1
            pygame.mixer.music.load(song[cnt])
            pygame.mixer.music.play(-1)
            a = 1
            break
        if event.type == pygame.MOUSEBUTTONDOWN and 685 <= mx <= 815 and 515 <= my <= 647:
            cnt += 1
            if cnt > len(song) - 1:
                cnt = 0
            pygame.mixer.music.load(song[cnt])
            pygame.mixer.music.play(-1)
            a = 1
            break
        if event.type == pygame.MOUSEBUTTONDOWN and 535 <= mx <= 660 and 515 <= my <= 647 and a == 1:
            a = 0
            pygame.mixer.music.pause()
            screen.blit(pause,(500,500))
            break
pygame.quit()   

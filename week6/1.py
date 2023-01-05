import pygame
import datetime
from math import pi, sin, cos
pygame.init()
image = pygame.image.load('3.png')
left = pygame.image.load('5.png')
right = pygame.image.load('4.png')
size = width, height = image.get_size()
screen = pygame.display.set_mode(size)
screen.fill((0,0,0))
color = (0,0,0)
clock = pygame.time.Clock()
done = False 

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0]- originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

r1,r2 = right.get_size()
l1,l2 = left.get_size()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    screen.blit(image,(0,0))
    pos = (screen.get_width() / 2, screen.get_height() / 2)
    t = datetime.datetime.now()
    second = t.second + 8
    minute = t.minute - 10
    clock.tick(60)
    theta = second * (360 / 60)
    blitRotate(screen, right, pos, (r1 ,r2), theta)
    theta = (minute + second / 60) * (360 / 60)
    blitRotate(screen, left, pos, (l1 / 2 ,l2 / 2), theta)
    pygame.draw.circle(screen, color, (width / 2, height / 2), 10)
pygame.quit()



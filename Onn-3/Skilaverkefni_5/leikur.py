import pygame
from random import randint

def randomColor():
    return [randint(0, 255), randint(0, 255), randint(0, 255)]

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 250
y = 250
width = 50
height = 50
vel = 2

running = True
color = randomColor()
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x-vel >= 0:
            x -= vel
        else:
            color = randomColor()

    if keys[pygame.K_RIGHT]:
        if x+vel+50 <= 500:
            x += vel
        else:
            color = randomColor()

    if keys[pygame.K_UP]:
        if y-vel >= 0:
            y -= vel
        else:
            color = randomColor()

    if keys[pygame.K_DOWN]:
        if y+vel+50 <= 500:
            y += vel
        else:
            color = randomColor()


    win.fill((0, 0, 0))
    pygame.draw.rect(win, (color), [x, y, width, height], 0)
    pygame.display.update()

pygame.quit()
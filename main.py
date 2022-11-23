import pygame
from Snake import *

pygame.init()
bounds = (800, 800)
screen = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
block_size = 40
snake = Snake(block_size, bounds)

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    snake.move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        snake.way(Direction.UP)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        snake.way(Direction.LEFT)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        snake.way(Direction.DOWN)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        snake.way(Direction.RIGHT)
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    screen.fill((0,0,0))
    snake.draw(pygame,screen)
    pygame.display.flip()


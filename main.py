import pygame
from Snake import *
from Food import Food

pygame.init()
bounds = (800, 800)
screen = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
block_size = 40
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)
fonts = pygame.font.SysFont('comicsans', 40, True)

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    snake.move()
    snake.snake_reached_food(food)
    keys = pygame.key.get_pressed()


    # Условие на самопоедание всегда выдает True, поэтому игра крашится
    if snake.check_bounds() == True or snake.snake_eats_itself() == True:
        text = fonts.render('Game Over... To restart press ENTER', True, (255,255,255))
        screen.blit(text,(400,400))
        pygame.display.update()
        pygame.time.delay(1000)
        snake.respawn()
        food.respawn()


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
    food.draw(pygame,screen)
    pygame.display.flip()


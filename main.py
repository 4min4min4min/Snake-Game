import pygame
from datetime import date
from Snake import *
from Food import Food

def showscore():
    your_score = fonts.render('Your score: ' + str(snake.score), True, (255, 255, 255))
    screen.blit(your_score, (300, 330))
def gameover():
    game_over = fonts.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over, (310, 300))
def showrecord():
    f = open('scores.txt', 'r')
    file = f.readlines()
    record = int(max(file))
    f.close()
    your_record = fonts.render('Your record: ' + str(record), True, (255, 255, 255))
    screen.blit(your_record, (300, 350))

def updateFile():
    file = open('scores.txt', 'a')
    file.write(str(snake.score)+'\n')
    file.close()





pygame.init()
score = 0
bounds = (800, 800)
screen = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
block_size = 40
snake = Snake(block_size, bounds, score)
food = Food(block_size, bounds)
fonts = pygame.font.SysFont('arial', 20, True)

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    snake.move()
    snake.snake_reached_food(food)
    if snake.check_bounds() == True or snake.snake_eats_itself() == True:
        gameover()
        showscore()
        showrecord()
        updateFile()
        pygame.display.update()
        pygame.time.delay(1500)
        snake.score = 0
        snake.respawn()
        food.respawn()

    screen.fill((0,0,0))
    snake.draw(pygame,screen)
    food.draw(pygame,screen)
    pygame.display.flip()





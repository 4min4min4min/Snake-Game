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
    f = open('scores.txt', 'r')  # opens the file in read mode
    file = f.readlines()  # reads all the lines in as a list
    record = int(max(file))  # gets the first line of the file
    f.close()
    your_record = fonts.render('Your record: ' + str(record), True, (255, 255, 255))
    screen.blit(your_record, (300, 350))

def updateFile():
    '''f = open('scores.txt', 'r')  # opens the file in read mode
    file = f.readlines()  # reads all the lines in as a list
    last = int(file[0])  # gets the first line of the file

    if last < int(snake.score): # sees if the current score is greater than the previous best
    f.close()'''  # closes/saves the file
    file = open('scores.txt', 'a')  # reopens it in write mode
    file.write(str(snake.score)+'\n')  # writes the best score
    file.close()  # closes/saves the file





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
'''text1 = fonts.render('Привет, Сяма', True, (255,255,255))
text2 = fonts.render('Это Папа', True, (255,255,255))
screen.blit(text1,(350,400))
screen.blit(text2,(375,430))
pygame.display.update()
pygame.time.delay(5000)'''
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
    # Условие на самопоедание всегда выдает True, поэтому игра крашится
    if snake.check_bounds() == True or snake.snake_eats_itself() == True:
        #game_over = fonts.render('GAME OVER', True, (255,255,255))
        #your_score = fonts.render('Your score: '+str(score), True, (255, 255, 255))
        #screen.blit(game_over,(310,300))
        #screen.blit(your_score, (300, 330))
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





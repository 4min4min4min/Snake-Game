import pygame
from pygame import mixer
from snake import *
from food import Food

def gameover():
    game_over_place = (300, 260)
    your_score_place = (330, 350)
    your_record_place = (330, 400)
    f = open('scores.txt', 'r')
    file = f.readlines()
    record = int(max(file))
    f.close()
    game_over = gg_fonts.render('GAME OVER', True, (255, 255, 255))
    your_score = fonts.render('Your Score:  '+str(snake.score), True, (255, 255, 255))
    your_record = fonts.render('Your Record:  '+str(record), True, (255, 255, 255))
    screen.blit(game_over, game_over_place)
    screen.blit(your_score, your_score_place)
    screen.blit(your_record, your_record_place)



def updateFile():
    file = open('scores.txt', 'a')
    file.write(str(snake.score)+'\n')
    file.close()





pygame.init()
mixer.init()
mixer.music.load('mainsong.ogg')
mixer.music.set_volume(0.7)
mixer.music.play(100)
score = 0
bounds = (800, 800)
screen = pygame.display.set_mode(bounds)
icon = pygame.image.load('snake.png')
pygame.display.set_caption("Snake")
pygame.display.set_icon(icon)
block_size = 40
snake = Snake(block_size, bounds, score)
food = Food(block_size, bounds)
fonts = pygame.font.SysFont('8-BIT WONDER', 30, True)
gg_fonts = pygame.font.SysFont('8-BIT WONDER', 45, True)
pause_text = gg_fonts.render('PRESS ENTER TO CONTINUE', True, (255,255,255))

playing, pause = True, False
running = True
state = playing
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = pause
            if event.key == pygame.K_RETURN:
                state = playing

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
        running = False

    if state == playing:
        mixer.music.unpause()
        snake.move()
        snake.snake_reached_food(food)
        if snake.check_bounds() == True or snake.snake_eats_itself() == True:
            gameover()
            updateFile()
            pygame.display.update()
            pygame.time.delay(1500)
            snake.score = 0
            snake.respawn()
            food.respawn()

        screen.fill((0,0,0))
        snake.draw(pygame,screen)
        food.draw(pygame,screen)
    elif state == pause:
        mixer.music.pause()
        screen.blit(pause_text,(150,260))
    pygame.display.flip()





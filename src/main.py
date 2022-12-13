import pygame
from pygame import mixer
from snake import *
from food import Food


def gameover():
    game_over_place = (300, 260)
    your_score_place = (330, 350)
    your_record_place = (330, 400)
    f = open('../res/scores.txt', 'r')
    file = f.readlines()
    record = int(max(file))
    f.close()
    game_over = gg_fonts.render('GAME OVER', True, (255, 255, 255))
    your_score = fonts.render('Your Score:  ' + str(snake.score), True, (255, 255, 255))
    your_record = fonts.render('Your Record:  ' + str(record), True, (255, 255, 255))
    screen.blit(game_over, game_over_place)
    screen.blit(your_score, your_score_place)
    screen.blit(your_record, your_record_place)


def updateFile():
    file = open('../res/scores.txt', 'a')
    file.write(str(snake.score) + '\n')
    file.close()


def draw_grass():
    grass_color1 = (167, 209, 61)
    grass_color2 = (175, 215, 70)
    for row in range(20):
        for col in range(20):
            grass_rect = pygame.Rect(col * block_size, row * block_size, block_size, block_size)
            color = grass_color1 if (row + col) % 2 == 0 else grass_color2
            pygame.draw.rect(screen, color, grass_rect)


pygame.init()

# music and sounds
mixer.init()
mixer.music.load('res/mainsong.ogg')
mixer.music.set_volume(0.5)
mixer.music.play(100)

# classes parameters
score = 0
bounds = (800, 800)
block_size = 40

# visual
screen = pygame.display.set_mode(bounds)
icon = pygame.image.load('../res/snake.png')
pygame.display.set_caption("Snake")
pygame.display.set_icon(icon)
apple = pygame.image.load('../res/apple.png').convert_alpha()

# classes
snake = Snake(block_size, bounds, score)
food = Food(block_size, bounds)

# fonts
fonts = pygame.font.SysFont('8-BIT WONDER', 30, True)
gg_fonts = pygame.font.SysFont('8-BIT WONDER', 45, True)
pause_text = gg_fonts.render('PRESS ENTER TO CONTINUE', True, (255, 255, 255))

playing, pause = True, False
running = True
state = playing


def draw_menu(current_item):
    red = (255, 0, 0)
    white = (255, 255, 255)

    x_coord = 150
    y_coord = 260
    y_offset = 60
    continue_text = gg_fonts.render('Continue', True, red if current_item == 0 else white)
    screen.blit(continue_text, (x_coord, y_coord))
    y_coord += y_offset

    champions = gg_fonts.render('Champions', True, red if current_item == 1 else white)
    screen.blit(champions, (x_coord, y_coord))
    y_coord += y_offset

    exit = gg_fonts.render('Exit', True, red if current_item == 2 else white)
    screen.blit(exit, (x_coord, y_coord))
    y_coord += y_offset


def menu():
    global running, state, playing, pause, food, apple, mixer
    mixer.music.pause()
    menu_running = True
    current_item = 0
    max_items = 3
    while menu_running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu_running = False

        keys = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        if keys[pygame.K_8]:
            menu_running = False
        elif keys[pygame.K_DOWN]:
            current_item += 1
            current_item %= max_items
        elif keys[pygame.K_UP]:
            current_item -= 1
            current_item %= max_items
        elif keys[pygame.K_ESCAPE]:
            menu_running = False
            running = False
        elif keys[pygame.K_RETURN]:
            if current_item == 0:
                menu_running = False
            elif current_item == 1:
                running = False
                menu_running = False
            elif current_item == 2:
                pass

        draw_menu(current_item)
        pygame.display.flip()

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
        running = False
    if keys[pygame.K_RETURN]:
        state = playing
    if keys[pygame.K_SPACE]:
        menu()

    if state == playing:
        mixer.music.unpause()
        snake.move()
        snake.snake_reached_food(food)
        if snake.check_bounds() == True or snake.snake_eats_itself() == True:
            gameover()
            if snake.score > 0:
                updateFile()
            pygame.display.update()
            pygame.time.delay(1500)
            snake.score = 0
            snake.respawn()
            food.respawn()

        screen.fill((0, 0, 0))
        draw_grass()
        snake.draw(pygame, screen)
        food.draw(pygame, screen, apple)
    elif state == pause:
        mixer.music.pause()
        screen.blit(pause_text, (150, 260))
    pygame.display.flip()

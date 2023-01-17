from pygame import mixer

from food import Food
from snake import *


def gameover():
    game_over_place = (300, 260)
    your_score_place = (330, 350)
    your_record_place = (330, 400)
    f = open('res/scores.txt', 'r')
    file = f.readlines()
    record = int(max(file))
    f.close()
    game_over = gg_fonts.render('GAME OVER', True, (255, 255, 255))
    your_score = fonts.render('Your Score:  ' + str(snake.score), True, (255, 255, 255))
    your_record = fonts.render('Your Record:  ' + str(record), True, (255, 255, 255))
    screen.blit(game_over, game_over_place)
    screen.blit(your_score, your_score_place)
    screen.blit(your_record, your_record_place)


def update_file():
    file = open('res/scores.txt', 'a')
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

# game settings
complexity = 'Medium'
snake_speed = 100
volume = 0.5
volume_value = 100

# music and sounds
mixer.init()
mixer.music.load('res/mainsong.ogg')
mixer.music.set_volume(volume)
mixer.music.play(100)

# classes parameters
score = 0
bounds = (800, 800)
block_size = 40

# visual
screen = pygame.display.set_mode(bounds)
icon = pygame.image.load('res/snake.png')
pygame.display.set_caption("Snake")
pygame.display.set_icon(icon)
apple = pygame.image.load('res/apple.png').convert_alpha()

# classes
snake = Snake(block_size, bounds, score)
food = Food(block_size, bounds)

# fonts
fonts = pygame.font.Font('Game Font.ttf', 30)
gg_fonts = pygame.font.Font('Game Font Bold.ttf', 45)

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

    options_menu = gg_fonts.render('Options', True, red if current_item == 1 else white)
    screen.blit(options_menu, (x_coord, y_coord))
    y_coord += y_offset

    champions = gg_fonts.render('Champions', True, red if current_item == 2 else white)
    screen.blit(champions, (x_coord, y_coord))
    y_coord += y_offset

    exit = gg_fonts.render('Exit', True, red if current_item == 3 else white)
    screen.blit(exit, (x_coord, y_coord))
    y_coord += y_offset


def draw_options(selected_item):
    global complexity, volume_value
    red = (255, 0, 0)
    white = (255, 255, 255)

    x_coord = 150
    y_coord = 260
    y_offset = 60
    x_offset = 260
    difficulty_level = gg_fonts.render('Difficult', True, red if selected_item == 0 else white)
    screen.blit(difficulty_level, (x_coord, y_coord))
    x_coord += x_offset
    difficulty_regime = gg_fonts.render(complexity, True, red if selected_item == 0 else white)
    screen.blit(difficulty_regime, (x_coord, y_coord))
    y_coord += y_offset
    x_coord -= x_offset

    volume_text = gg_fonts.render('Volume', True, red if selected_item == 1 else white)
    screen.blit(volume_text, (x_coord, y_coord))
    x_coord += x_offset
    volume_regime = gg_fonts.render(str(volume_value), True, red if selected_item == 1 else white)
    screen.blit(volume_regime, (x_coord, y_coord))
    y_coord += y_offset
    x_coord -= x_offset

    back_text = gg_fonts.render('Back', True, red if selected_item == 2 else white)
    screen.blit(back_text, (x_coord, y_coord))
    y_coord += y_offset


def options():
    global snake_speed, running, keys1, complexity, volume, volume_value
    mixer.music.pause()
    options_running = True
    selected_item = 0
    max_items = 3
    while options_running:
        pygame.time.delay(100)
        keys1 = pygame.key.get_pressed()
        screen.fill((0, 0, 0))

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                options_running = False

        if keys1[pygame.K_DOWN]:
            selected_item += 1
            selected_item %= max_items

        elif keys1[pygame.K_UP]:
            selected_item -= 1
            selected_item %= max_items

        elif keys1[pygame.K_ESCAPE]:
            options_running = False

        elif keys1[pygame.K_RETURN]:
            if selected_item == 0:
                pass
            elif selected_item == 1:
                pass
            elif selected_item == 2:
                options_running = False

        elif keys1[pygame.K_LEFT]:
            if selected_item == 0:
                if complexity == 'Medium':
                    complexity = 'Easy'
                    snake_speed = 140
                elif complexity == 'Hard':
                    complexity = 'Medium'
                    snake_speed = 100
                elif complexity == 'Easy':
                    pass
            elif selected_item == 1:
                if volume_value == 0:
                    pass
                else:
                    volume -= 0.02
                    volume_value -= 1

        elif keys1[pygame.K_RIGHT]:
            if selected_item == 0:
                if complexity == 'Medium':
                    complexity = 'Hard'
                    snake_speed = 80
                elif complexity == 'Easy':
                    complexity = 'Medium'
                    snake_speed = 100
                elif complexity == 'Hard':
                    pass
            elif selected_item == 1:
                if volume_value == 100:
                    pass
                else:
                    volume += 0.02
                    volume_value += 1

        draw_options(selected_item)
        pygame.display.flip()


def menu():
    global running, state, playing, pause, food, apple
    mixer.music.pause()
    menu_running = True
    current_item = 0
    max_items = 4
    while menu_running:
        pygame.time.delay(100)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = True
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
                options()
            elif current_item == 2:
                pass
            elif current_item == 3:
                running = False
                menu_running = False

        draw_menu(current_item)
        pygame.display.flip()


while running:
    game_difficult = pygame.time.delay(snake_speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys1 = pygame.key.get_pressed()
    if keys1[pygame.K_UP] or keys1[pygame.K_w]:
        snake.way(Direction.UP)
    elif keys1[pygame.K_LEFT] or keys1[pygame.K_a]:
        snake.way(Direction.LEFT)
    elif keys1[pygame.K_DOWN] or keys1[pygame.K_s]:
        snake.way(Direction.DOWN)
    elif keys1[pygame.K_RIGHT] or keys1[pygame.K_d]:
        snake.way(Direction.RIGHT)
    if keys1[pygame.K_RETURN]:
        state = playing
    if keys1[pygame.K_SPACE] or keys1[pygame.K_ESCAPE]:
        menu()

    if state == playing:
        mixer.music.unpause()
        snake.move()
        snake.snake_reached_food(food)
        if snake.check_bounds() or snake.snake_eats_itself():
            gameover()
            if snake.score > 0:
                update_file()
            pygame.display.update()
            pygame.time.delay(1500)
            snake.score = 0
            snake.respawn()
            food.respawn()

        screen.fill((0, 0, 0))
        draw_grass()
        snake.draw(pygame, screen)
        food.draw(pygame, screen, apple)
    pygame.display.flip()

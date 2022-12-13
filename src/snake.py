from enum import Enum

import pygame


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    length = None
    direction = None
    body = None
    block_size = None
    bounds = None
    color = (0, 49, 83)
    score = None

    def __init__(self, block_size, bounds, score):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()
        self.score = score

        self.head_up = pygame.image.load('../res/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('../res/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('../res/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('../res/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('../res/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('../res/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('../res/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('../res/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('../res/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('../res/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('../res/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('../res/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('../res/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('../res/body_bl.png').convert_alpha()

    def respawn(self):
        self.length = 5
        self.body = [(240, 400), (280, 400), (320, 400), (360, 400), (400, 400)]
        self.direction = Direction.RIGHT

    def get_next_head(self):
        current_head = self.body[-1]
        if self.direction == Direction.DOWN:
            return current_head[0], current_head[1] + self.block_size
        if self.direction == Direction.UP:
            return current_head[0], current_head[1] - self.block_size
        if self.direction == Direction.RIGHT:
            return current_head[0] + self.block_size, current_head[1]
        if self.direction == Direction.LEFT:
            return current_head[0] - self.block_size, current_head[1]

    def move(self):
        self.body.append(self.get_next_head())
        if self.length < len(self.body):
            self.body.pop(0)

    def way(self, direction):
        if self.direction == Direction.DOWN and direction != Direction.UP:
            self.direction = direction
        elif self.direction == Direction.UP and direction != Direction.DOWN:
            self.direction = direction
        elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
            self.direction = direction
        elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
            self.direction = direction

    def update_head_graphics(self):
        if self.direction == Direction.RIGHT:
            self.head = self.head_right
        if self.direction == Direction.LEFT:
            self.head = self.head_left
        if self.direction == Direction.UP:
            self.head = self.head_up
        if self.direction == Direction.DOWN:
            self.head = self.head_down

    def update_tail_graphics(self):
        part_before_tail = self.body[1]
        tail_part = self.body[0]
        if tail_part[0] == part_before_tail[0] + 40 and tail_part[1] == part_before_tail[1]:
            self.tail = self.tail_right
        if tail_part[0] == part_before_tail[0] - 40 and tail_part[1] == part_before_tail[1]:
            self.tail = self.tail_left
        if tail_part[0] == part_before_tail[0] and tail_part[1] == part_before_tail[1] + 40:
            self.tail = self.tail_down
        if tail_part[0] == part_before_tail[0] and tail_part[1] == part_before_tail[1] - 40:
            self.tail = self.tail_up

    def draw(self, pygame, screen):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, part in enumerate(self.body):
            part_rect = pygame.Rect(part[0], part[1], self.block_size, self.block_size)
            if index == 0:
                screen.blit(self.tail, part_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.head, part_rect)
            else:
                next_part = self.body[index - 1]
                previous_part = self.body[index + 1]
                if next_part[1] == previous_part[1]:
                    screen.blit(self.body_horizontal, part_rect)
                if next_part[0] == previous_part[0]:
                    screen.blit(self.body_vertical, part_rect)
                else:
                    if next_part[0] == part[0] and previous_part[0] == part[0] + 40 and next_part[1] == part[1] - 40 and \
                            previous_part[1] == part[1] or next_part[0] == part[0] + 40 and previous_part[0] == part[
                        0] and next_part[1] == part[1] and previous_part[1] == part[1] - 40:
                        screen.blit(self.body_tr, part_rect)
                    if next_part[0] == part[0] - 40 and previous_part[0] == part[0] and next_part[1] == part[1] and \
                            previous_part[1] == part[1] - 40 or next_part[0] == part[0] and previous_part[0] == part[
                        0] - 40 and next_part[1] == part[1] - 40 and previous_part[1] == part[1]:
                        screen.blit(self.body_tl, part_rect)
                    if next_part[0] == part[0] and previous_part[0] == part[0] - 40 and next_part[1] == part[1] + 40 and \
                            previous_part[1] == part[1] or next_part[0] == part[0] - 40 and previous_part[0] == part[
                        0] and next_part[1] == part[1] and previous_part[1] == part[1] + 40:
                        screen.blit(self.body_bl, part_rect)
                    if next_part[0] == part[0] + 40 and previous_part[0] == part[0] and next_part[1] == part[1] and \
                            previous_part[1] == part[1] + 40 or next_part[0] == part[0] and previous_part[0] == part[
                        0] + 40 and next_part[1] == part[1] + 40 and previous_part[1] == part[1]:
                        screen.blit(self.body_br, part_rect)

    def eat(self):
        self.length += 1

    def snake_reached_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            self.score += 1
            food.respawn()

    def snake_eats_itself(self):
        head = self.body[-1]
        has_eaten_tail = False

        for i in range(len(self.body) - 1):
            part = self.body[i]
            if head[0] == part[0] and head[1] == part[1]:
                has_eaten_tail = True
                break
        return has_eaten_tail

    def check_bounds(self):
        head = self.body[-1]

        if head[0] >= self.bounds[0]:
            return True
        if head[1] >= self.bounds[1]:
            return True

        if head[0] < 0:
            return True
        if head[1] < 0:
            return True

        return False

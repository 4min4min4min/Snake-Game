from enum import Enum


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


    def respawn(self):
        self.length = 5
        self.body = [(240, 400), (280, 400), (320, 400), (360, 400), (400, 400)]
        self.direction = Direction.RIGHT


    def draw(self, pygame, screen):
        for part in self.body:
            pygame.draw.rect(screen, self.color, (part[0], part[1], self.block_size, self.block_size))

    def move(self):
        current_head = self.body[-1]
        if self.direction == Direction.DOWN:
            next_head = (current_head[0], current_head[1] + self.block_size)
            self.body.append(next_head)
        if self.direction == Direction.UP:
            next_head = (current_head[0], current_head[1] - self.block_size)
            self.body.append(next_head)
        if self.direction == Direction.RIGHT:
            next_head = (current_head[0] + self.block_size, current_head[1])
            self.body.append(next_head)
        if self.direction == Direction.LEFT:
            next_head = (current_head[0] - self.block_size, current_head[1])
            self.body.append(next_head)

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

    def eat(self):
        self.length += 1


    def snake_reached_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            self.score +=1
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
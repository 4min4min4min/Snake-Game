import random


class Food:
    block_size = None
    color = (255, 255, 240)
    x = 0
    y = 0
    bounds = None
    fruit = 0

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, screen, apple, blueberry, cherry, lemon):
        # pygame.draw.rect(screen, self.color, (self.x, self.y, self.block_size, self.block_size))
        #screen.blit(apple, (self.x, self.y, self.block_size, self.block_size))
        if self.fruit == 0:
            screen.blit(apple, (self.x, self.y, self.block_size, self.block_size))
        elif self.fruit == 1:
            screen.blit(blueberry, (self.x, self.y, self.block_size, self.block_size))
        elif self.fruit == 2:
            screen.blit(cherry, (self.x, self.y, self.block_size, self.block_size))
        elif self.fruit == 3:
            screen.blit(lemon, (self.x, self.y, self.block_size, self.block_size))


    def respawn(self):
        self.fruit = random.randint(0, 3)
        blocks_in_x = (self.bounds[0]) / self.block_size
        blocks_in_y = (self.bounds[1]) / self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size

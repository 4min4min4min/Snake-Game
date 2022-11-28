import random

class Food:
    block_size = None
    color = (255,255,240)
    x = 0
    y = 0
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw (self, pygame, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size
        blocks_in_y = (self.bounds[1])/self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size #and !=
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size
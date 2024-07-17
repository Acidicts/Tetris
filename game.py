from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.blocks[2]
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return random.choice(self.blocks)

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside():
            self.current_block.move(0, -1)

    def move_block_down(self):
        self.current_block.move(1, 0)
        if self.block_inside():
            self.current_block.move(-1, 0)

    def rotate_block(self):
        self.current_block.rotate()
        if self.block_inside():
            if self.current_block.rotation == 0:
                self.current_block.rotation = 3
            else:
                self.current_block.rotation -= 1

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) is False:
                return False

        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

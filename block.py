import pygame
from colors import Colors


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation = 0
        self.colors = Colors.get_cell_colors()

    def draw(self, win):
        tiles = self.colors[self.rotation]

        for tile in tiles:
            cell_rect = pygame.Rect(
                tile.row * self.cell_size + 1,
                tile.column * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(win, self.colors[self.id], cell_rect)

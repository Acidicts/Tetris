import pygame
from colors import Colors
from position import Position


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30

        self.row_offset = 0
        self.column_offset = 0

        self.rotation = 0
        self.colors = Colors.get_cell_colors()

    def rotate(self):
        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0

    def move(self, columns, rows):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation]
        moved_tiles = []
        for position in tiles:
            new_pos = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(new_pos)
        return moved_tiles

    def draw(self, win):
        tiles = self.get_cell_positions()

        for tile in tiles:
            cell_rect = pygame.Rect(
                tile.row * self.cell_size + 1,
                tile.column * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(win, self.colors[self.id], cell_rect)

import pygame
from grid import Grid
from blocks import LBlock

pygame.init()

dark_blue = (44, 44, 127)

win = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    win.fill(dark_blue)
    game_grid.draw(win)



    pygame.display.update()
    clock.tick(60)

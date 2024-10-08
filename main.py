import pygame
from grid import Grid
from blocks import *
from game import Game

pygame.init()

dark_blue = (44, 44, 127)

win = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_UP:
                game.rotate_block()
            if event.key == pygame.K_DOWN:
                game.move_block_down()

    win.fill(dark_blue)
    game.draw(win)

    pygame.display.update()
    clock.tick(60)

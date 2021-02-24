import pygame
from pygame.locals import *


def draw_block():
    surface.fill((110, 110, 5))  # it remove the previous blocks
    surface.blit(block, (block_x, block_y))  # determine the block position
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()  # initialise the pygame module

    surface = pygame.display.set_mode((500, 500))  # game window size
    surface.fill((110, 110, 5))  # window color (rGB format)

    block = pygame.image.load("resources/block.jpg").convert()  # image load

    block_x, block_y = 100, 100

    pygame.display.flip()  # it update the window

    running = True
    # event loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False  # exit
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()

            elif event.type == QUIT:
                running = False

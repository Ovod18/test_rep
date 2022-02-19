"""This module contains the main function of 'snake' game

    :platform: Linux
    :author: Ovod18

    |
"""

import pygame
import random
import time
import math
import items
import surface

FPS = 60
INF_HEIGHT : int
"""The information line height.

    |
"""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

def main(dw, dh, sw, ss):
    """The main function of 'snake' game.

    :param int dw: The display width.
    :param int dh: The display height.
    :param int sw: The snake width.
    :param int ss: The snake speed.

    |
    """

    INF_HEIGHT = sw

    # Creating the main window.
    pygame.init()
    screen = pygame.display.set_mode((dw, dh))
    pygame.display.set_caption("My snake")

    clock = pygame.time.Clock()

    # Setting snakes properties
    my_snake = items.Snake(sw)
    body = my_snake.get_body()
    head_pos = my_snake.get_head_pos()

    # Setting other values
    course = ""
    apple = items.Food(sw, dw, dh, INF_HEIGHT)
    info = surface.InfoString(screen, sw)
    play_ground = surface.PlayGround(screen, info)

    # Creating the game cycle.
    state = "running"
    while state != "quit":
        # Keys binding
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                state = "quit"
            if event.type == pygame.KEYDOWN:
                if (event.key==pygame.K_LEFT) and (course!="RIGHT"):
                    course = "LEFT"
                elif (event.key==pygame.K_RIGHT) and (course!="LEFT"):
                    course = "RIGHT"
                elif (event.key==pygame.K_UP) and (course!="DOWN"):
                    course = "UP"
                elif (event.key==pygame.K_DOWN) and (course!="UP"):
                    course = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    state = "pause"
                elif event.key == pygame.K_r:
                    state = "running"

        if state == "running":

            # Snake movement
            my_snake.set_course(course, ss)
            my_snake.move(play_ground)

            # Snake eats food
            h_pos = my_snake.get_head_pos()
            a_pos = apple.get_pos()
            a_radius = apple.get_size() / 2
            d = items.dist(a_pos, h_pos)
            if d < (sw / 2):
                color = apple.get_color()
                my_snake.eat(apple.get_size(), color)
                info.up_score(apple.get_size())

                #if snake is very big
                if not my_snake.is_crit_len(play_ground):
                    apple.set_size(sw, "r")
                else:
                    apple.set_size(sw, 0)
                apple.set_pos(body, sw)
                apple.set_color()

            # Wasted by collision the snakes body.
            if my_snake.is_collision_with_body():
                font = pygame.font.Font(None, sw)
                text = "WASTED"
                message = font.render(text, True, RED)
                screen.blit(message, [dw/2, dh/2])
                pygame.display.update()
                time.sleep(5)
                state = "quit"

            # Draw the screen with black color.
            screen.fill(BLACK)

            # Rendering info string
            info.draw(screen)

            # Rendering snake
            my_snake.draw(screen)

            # Rendering food
            apple.draw(screen)

            pygame.display.update()
            clock.tick(FPS)

    pygame.quit()

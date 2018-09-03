import pygame
import random

pygame.init()

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def snake_block(color, x, y, w, h):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def apple(color, x, y, w, h):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

def game_loop():
    x_change = random.choice([-5, 5])
    y_change = 0
    snake_width = 20
    snake_x = 0
    snake_y = 0
    snake_body = [[80, 100], [80, 120], [80, 140], [80, 160]]
    x_change = snake_width
    y_change = 0

    # snake_body = {1, 2, 3, 4}
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -snake_width
                    y_change = 0
                if event.key == pygame.K_d:
                    x_change = snake_width
                    y_change = 0
                if event.key == pygame.K_s:
                    y_change = snake_width
                    x_change = 0
                if event.key == pygame.K_w:
                    y_change = -snake_width
                    x_change = 0

        gameDisplay.fill(white)
        snake_x = x_change + snake_body[0][0]
        snake_y = y_change + snake_body[0][1]
        s_block = [snake_x, snake_y]
        for each in snake_body:
            snake_block(red, each[0], each[1], snake_width, snake_width)
        snake_body.pop()
        snake_body.insert(0, s_block)

        del snake_body[-1]


        pygame.display.update()
        clock.tick(15)


game_loop()

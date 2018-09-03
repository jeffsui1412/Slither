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

    apple_width = 20
    apple_choice = []
    for each in range(display_width-20):
        if each % 20 == 0:
            apple_choice.append(each)
    apple_x = random.choice(apple_choice)
    apple_y = random.choice(apple_choice)

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
        #add tail
        snake_body.insert(0, s_block)
        #blit snake body
        for each in snake_body:
            snake_block(red, each[0], each[1], snake_width, snake_width)
        #remove tail
        del snake_body[-1]
        #check wall
        if snake_body[0][0] < 0 or snake_body[0][0] > display_width - snake_width or snake_body[0][1] < 0 or snake_body[0][1] > display_height - snake_width:
            pygame.quit()
            quit()
        #blit apple
        if snake_body[0] == apple_x and snake_body[1] == apple_y:
            apple_x = random.choice(apple_choice)
            apple_y = random.choice(apple_choice)
        apple(green, apple_x, apple_y, apple_width, apple_width)
        pygame.display.update()
        clock.tick(10)


game_loop()

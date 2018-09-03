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

def apple_ran():
    return 20 * random.randint(0, 30)

def game_loop():
    fps = 10
    x_change = random.choice([-5, 5])
    y_change = 0
    snake_width = 20
    snake_x = 0
    snake_y = 0
    snake_body = [[80, 100], [80, 120], [80, 140], [80, 160]]
    x_change = snake_width
    y_change = 0
    apple_width = 20

    apple_x = apple_ran()
    apple_y = apple_ran()

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    dir = 0
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if dir != 2:
                        x_change = -snake_width
                        y_change = 0
                        dir = LEFT
                if event.key == pygame.K_d:
                    if dir != 4:
                        x_change = snake_width
                        y_change = 0
                        dir = RIGHT
                if event.key == pygame.K_s:
                    if dir != 1:
                        y_change = snake_width
                        x_change = 0
                        dir = DOWN
                if event.key == pygame.K_w:
                    if dir != 3:
                        y_change = -snake_width
                        x_change = 0
                        dir = UP

        snake_x = x_change + snake_body[0][0]
        snake_y = y_change + snake_body[0][1]
        s_block = [snake_x, snake_y]
        eat = False
        #white game display
        gameDisplay.fill(white)

        #add head
        snake_body.insert(0, s_block)

        #blit snake body
        for each in snake_body:
            snake_block(red, each[0], each[1], snake_width, snake_width)

        #check wall
        if snake_body[0][0] < 0 or snake_body[0][0] > display_width - snake_width or snake_body[0][1] < 0 or snake_body[0][1] > display_height - snake_width:
            pygame.quit()
            quit()

        #check apple
        if snake_body[0][0] == apple_x and snake_body[0][1] == apple_y:
            apple_x = apple_ran()
            apple_y = apple_ran()
            eat = True
        #check snake body
        if snake_body[0] in snake_body[1:]:
            pygame.quit()
            quit()

        #remove tail
        if not eat:
            snake_body.pop()
        #add apple
        apple(green, apple_x, apple_y, apple_width, apple_width)

        #check length
        if len(snake_body) >= 10:
            fps += 5
        pygame.display.update()
        clock.tick(13)


game_loop()
